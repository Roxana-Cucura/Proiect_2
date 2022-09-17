from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/')

buttons= chrome.find_element(By.PARTIAL_LINK_TEXT, 'Buttons')
buttons.click()
sleep(2)

back = chrome.find_element(By.ID, 'logo')
sleep(2)
back.click()
sleep(2)

radio= chrome.find_element(By.PARTIAL_LINK_TEXT, 'Radio Button')
radio.click()
sleep(2)

chrome.quit()