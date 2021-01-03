# Aus dieser Playlist
# https://www.youtube.com/playlist?list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ

import os
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

tickers = []
DAX_tickers = []

def LoadLocalData(reload_DAX = False, pickle_dataframe = "DAX_tickers.pickle", start = dt.datetime(1980,1,1), end = dt.datetime.now()):
    import pickle
    global DAX_tickers,tickers

    if reload_DAX:
        DAX_tickers, tickers = download_DAX_tickers()
    else:
        with open("data/pickled_dfs/{}".format(pickle_dataframe), 'rb') as f:
            tickers = pickle.load(f)

    for ticker in tickers:
        if not os.path.isfile('data/stock_dfs/_{}.csv'.format(ticker)):
            RetrieveOnlineData(ticker)
            print("Getting {} online".format(ticker))
        else:
            print("{} is already in the directory".format(ticker))

def RetrieveOnlineData(ticker, source = "yahoo", start = dt.datetime(1980,1,1), end = dt.datetime.now()):
    if not os.path.exists('data/stock_dfs'):
        os.makedirs('data/stock_dfs')

    web.DataReader(ticker, source, start, end).to_csv('data/stock_dfs/_{}.csv'.format(ticker))

def GetNameFromTicker(ticker):
    import requests
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(ticker)
    source = requests.get(url).json()

    #das ist bestimmt mega ineffizient, geht wohl auch stattdessen mit yfinance
    for x in source['ResultSet']['Result']:
        if x['symbol'] == ticker:
            return x['name']

def compile_data(pickle_dataframe, new_name):
    import pickle
    import os

    with open("data/pickled_dfs/{}".format(pickle_dataframe), 'rb') as f:
        tickers = pickle.load(f)
    new_dataframe = pd.DataFrame()

    for count, ticker in enumerate(tickers):
        if os.path.exists('data/stock_dfs/_{}.csv'.format(ticker)):
            old_dataframe = pd.read_csv('data/stock_dfs/_{}.csv'.format(ticker))
        else:
            print("{}.csv is not accessible. Does it exist?".format(ticker))

        old_dataframe.set_index('Date', inplace=True)
        old_dataframe.rename(columns = {'Adj Close': ticker}, inplace = True)
        old_dataframe.drop(['Open','High','Low','Close','Volume'], 1, inplace = True)

        if new_dataframe.empty:
            new_dataframe = old_dataframe
        else:
            new_dataframe = new_dataframe.join(old_dataframe, how='outer')

        print("included _{}.csv".format(ticker))

    print(new_dataframe)
    if os.path.exists('data/compiled_dfs/'):
        new_dataframe.to_csv('data/compiled_dfs/_{}.csv'.format(new_name))
    else:
        os.makedirs('data/compiled_dfs/')
        new_dataframe.to_csv('data/compiled_dfs/_{}.csv'.format(new_name))

def download_DAX_tickers():         #von Wikipedia
    import bs4 as bs
    import pickle
    import requests

    resp = requests.get('https://en.wikipedia.org/wiki/DAX#Components')
    soup = bs.BeautifulSoup(resp.text, features="lxml")
    table = soup.find('table',{'class':'wikitable sortable','id':'constituents'})

    global DAX_tickers
    if not os.path.exists("data/pickled_dfs/"):
        os.makedirs("data/pickled_dfs/")

    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[3].text
        DAX_tickers.append(ticker)
    with open ("data/pickled_dfs/DAX_tickers.pickle","wb") as f:
        pickle.dump(DAX_tickers, f)

    return DAX_tickers

def visualize_data(csv_dataframe):
    import numpy as np

    dataframe = pd.read_csv('data/{}'.format(csv_dataframe))
    df_correlation = dataframe.corr()

    ticker_names = []
    for ticker in dataframe:
        if ticker != 'Date':
            ticker_names.append(GetNameFromTicker(ticker))

    print(ticker_names)
    print(df_correlation.tail())

    data = df_correlation.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = ticker_names
    row_labels = ticker_names
    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1)

    plt.tight_layout()
    plt.show()

def ShowDay3():
    style.use('ggplot')
    dataframe = pd.read_csv('VanEck Esports.csv', parse_dates = True, index_col = 0)

    dataframe['100 mAverage'] = dataframe['Adj Close'].rolling(window=100, min_periods=25).mean()
    dataframe['20 mAverage'] = dataframe['Adj Close'].rolling(window=20).mean()

    print(dataframe.tail())

    ax1 = plt.subplot2grid((5,1),(0,0),rowspan=3)
    ax2 = plt.subplot2grid((4,1),(3,0),sharex=ax1)
    #dataframe[['100 mAverage','20 mAverage']].plot()

    ax1.plot(dataframe.index,dataframe['Adj Close'])
    ax1.plot(dataframe.index,dataframe['20 mAverage'])
    ax2.bar(dataframe.index,dataframe['Volume'])

    plt.show()

def ShowDay4():
    style.use('ggplot')
    dataframe = pd.read_csv('VanEck Esports.csv', parse_dates=True, index_col=0)

    #ohlc = open high low close
    df_ohlc = dataframe['Adj Close'].resample('10D').ohlc()
    df_volume = dataframe['Volume'].resample('10D').sum()

    df_ohlc.reset_index(inplace=True)
    df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
    #print(df_ohlc.tail())

    ax1 = plt.subplot2grid((5, 1), (0, 0), rowspan=3)
    ax2 = plt.subplot2grid((4, 1), (3, 0), sharex=ax1)
    ax1.xaxis_date()

    candlestick_ohlc(ax1,df_ohlc.values,2,'g')
    ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
    plt.show()

def ShowDay5():
    print("Day 5 - Automating getting the S&P 500 list \n ...aber wir holen uns den Dax! \n")
    download_DAX_tickers()
    print("Hier sind alle Ticker: {}".format(DAX_tickers))

def ShowDay6():
    print("Day 6 - Getting all company pricing data \n ...vom Dax! \n")
    LoadLocalData(start=dt.datetime(2019,1,1))

def ShowDay7():
    print("Day 7 - Combining S&P 500 into one DataFrame \n ...aber nicht S&P 500, sondern den Dax! \n")
    download_DAX_tickers()
    LoadLocalData(pickle_dataframe='DAX_tickers.pickle')
    compile_data('DAX_tickers.pickle',"DAX")

def ShowDay8():
    print("Day 8 - company correlation table \n")
    visualize_data('compiled_dfs/_DAX.csv')

def ShowDay9():
    print("Day 9 - Preprocessing data for Machine Learning \n")


ShowDay9()