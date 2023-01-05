import random
import os
import timeit
import pygame
import bs4
import requests

#TypeWithMe

#Features
# - Language selection (Deutsch / English)
# - Pull sentence from webpage database based on selection
# - Define 'difficulty' of sentence by analysing length & complexity
# - Countdown until typing input is accepted so player can get ready
# - Time and analyze typing
# - Give visual feedback for typing errors by marking mistakes red
# - Show progress bar and %
# - Count backspace corrections
# - When sentence is done show results by calculating a grade
# - Retry or New sentence/language


webpage = requests.get('https://www.randomsentencegen.com/')
soup = bs4.BeautifulSoup(webpage.text, features="lxml") #print(soup)
sentence = soup.find("p", class_="text-center sen-ex").get_text()
#print(sentence)

game_is_running = True

while game_is_running:
    pygame.display.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.update()

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_ESCAPE]:
        game_is_running = False

#TODO:
# 1. Satz in einem Fenster darstellen
# 2. User Input akzeptieren und auch darstellen
# 3. User Input und angezeigten Satz vergleichen
# 4. tbd