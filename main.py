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

username = driver.find_element_by_xpath('//input[@name="username"]')

# name = username
# name = password


driver.get('https://www.twitter.com/login')

