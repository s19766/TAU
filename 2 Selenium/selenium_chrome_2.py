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

logger.info('Find and click docs')

browser.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/div[1]/button").click()

logger.info('Go to User Guide')

browser.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/div[1]/div/div[1]/a").click()

time.sleep(2)

logger.info('Current url should be https://robotframework.org/robotframework/#user-guide')

if browser.current_url == "https://robotframework.org/robotframework/#user-guide":
    print("Url is okay")
else:
    print("There is something wrong with url :(")
# print(browser.current_url)

time.sleep(1)

logger.info('Find and open documentation for Builtin library - version 4.0')

browser.find_element(By.XPATH, '//*[@id="BuiltIn"]').click()
browser.find_element(By.XPATH, "/html/body/div/table[1]/tbody/tr[2]/td[2]/select/option[8]").click()
browser.find_element(By.XPATH, "/html/body/div/table[1]/tbody/tr[2]/td[2]/button").click()

logger.info('Current url should be https://robotframework.org/robotframework/4.0/libraries/BuiltIn.html')

if browser.current_url == "https://robotframework.org/robotframework/4.0/libraries/BuiltIn.html":
    print("Url is okay")
else:
    print("There is something wrong with url :(")
# print(browser.current_url)

browser.close()
