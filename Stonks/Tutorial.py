# Aus dieser Playlist
# https://www.youtube.com/playlist?list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

dataframe = web.DataReader("ESPO", 'yahoo', start, end)
dataframe.to_csv('VanEck Esports.csv')

dataframe = pd.read_csv('VanEck Esports.csv', parse_dates = True, index_col = 0)

#print(df.tail())
dataframe['Adj Close'].plot()
plt.show()