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

logger.info('Click login/register button')

button = browser.find_element(By.XPATH, "/html/body/div[2]/header/div/div/div/div[2]/div/div[2]/div/div[4]/a")
button.click()

time.sleep(1)

logger.info('Try to login')

login = browser.find_element(By.XPATH, '//*[@id="username"]')
login.send_keys("Login@wp.pl")
password = browser.find_element(By.XPATH, '//*[@id="password-log"]')
password.send_keys("Password")
action = browser.find_element(By.XPATH, "/html/body/main/div/div/div[3]/form/button")
action.click()

time.sleep(1)

logger.info('Find login error')

browser.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[2]")

time.sleep(2)

logger.info('Confirm the received error')

error_button = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/button")
error_button.click()

browser.close()
