from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/')

chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()
sleep(2)

address = chrome.find_elements(By.CLASS_NAME, 'form-control')
address[0].send_keys('Cluj')
sleep(2)

street = chrome.find_elements(By.CLASS_NAME, 'form-control')
street[1].send_keys('Crinului')
sleep(2)

city = chrome.find_elements(By.CLASS_NAME, 'form-control')
city[3].send_keys('Cluj, RO')
sleep(2)

zip_code = chrome.find_elements(By.CLASS_NAME, 'form-control')
zip_code[5].send_keys('12345')
sleep(2)

chrome.quit()

