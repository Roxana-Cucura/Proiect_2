from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://www.phptravels.net/')
sleep(2)

languages = chrome.find_element(By.ID, 'languages')
sleep(2)
languages.click()
sleep(2)

currency = chrome.find_element(By.ID, 'currency')
sleep(2)
currency.click()
sleep(2)

supplier = chrome.find_element(By.ID, 'supplier')
sleep(2)
supplier.click()
sleep(2)

agents = chrome.find_element(By.ID, 'agents')
sleep(2)
agents.click()
sleep(2)

tab = chrome.find_element(By.ID, 'Tab')
sleep(2)
tab.click()
sleep(2)

hotels_tab = chrome.find_element(By.ID, 'hotels-tab')
sleep(2)
hotels_tab.click()
sleep(2)

tours_tab = chrome.find_element(By.ID, 'tours-tab')
sleep(2)
tours_tab.click()
sleep(2)
