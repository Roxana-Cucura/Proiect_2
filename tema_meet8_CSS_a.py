from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/autocomplete')

chrome.find_element(By.CSS_SELECTOR, 'input#autocomplete').send_keys('Cl')
sleep(2)

chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('uj')
sleep(2)

chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="City"]').send_keys('Ro')
sleep(2)

chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*="City"]').send_keys('mania')
sleep(2)

chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Zip code"]').send_keys('123')
sleep(2)

chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*="Zip code"]').send_keys('45')
sleep(2)

chrome.quit()