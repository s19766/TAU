# Damian Eggert s19766

import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger('example')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

browser = webdriver.Chrome(service=Service(f"{os.path.abspath(os.getcwd())}/chromedriver"))

logger.info('Go to robotframework.org')

browser.get('https://robotframework.org/')

logger.info('Find facebook and twitter community site')

facebook = browser.find_element(By.XPATH, "/html/body/div/div[6]/div/div/div[2]/div[3]/a")
twitter = browser.find_element(By.XPATH, "/html/body/div/div[6]/div/div/div[2]/div[4]/a")

logger.info('Check if links are correct')

facebook_link = facebook.get_attribute("href")
twitter_link = twitter.get_attribute("href")

if facebook_link == "https://www.facebook.com/robotframeworkofficial" and \
        twitter_link == "https://twitter.com/robotframework":
    print("Both links are correct :)")
else:
    print("Something went wrong :/")

browser.close()
