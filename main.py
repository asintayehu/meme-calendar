import pandas as pd
# import tqdm.notebook as tqdm
import snscrape.modules.twitter as sntwitter

scraper = sntwitter.TwitterTrendsScraper()
tweets = []

for trend in scraper.get_items():
    print(trend)
    break


"""
import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver import Chrome

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)

# name_class = r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu
# password_class = r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu


driver.get('https://www.twitter.com/login')

"""




