from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('http://automationpractice.com/index.php')

checkbox = chrome.find_element(By.LINK_TEXT, 'Women')
sleep(2)
checkbox.click()
sleep(2)

