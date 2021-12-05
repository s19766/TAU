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

logger.info('Go to morele.net')

browser.get('https://www.morele.net/')
browser.maximize_window()

logger.info('Find search bar and click on it, type: "karty graficzne"')
time.sleep(1)

search_bar = browser.find_element(By.XPATH, "/html/body/div[2]/header/div/div/div/div[2]/div/div[1]/form/div/input")
search_bar.click()
time.sleep(1)
search_bar.send_keys("karty graficzne")
time.sleep(3)
search_button = browser.find_element(By.XPATH, "/html/body/div[2]/header/div/div/div/div[2]/div/div[1]/form/button")
search_button.click()
time.sleep(2)

logger.info('Check if you found: "karty graficzne"')

if browser.current_url == "https://www.morele.net/wyszukiwarka/0/0/,,,,,,,,,,,,/1/?q=karty%20graficzne":
    print("You found graphic cards")
else:
    print("Something went wrong :/")

browser.close()
