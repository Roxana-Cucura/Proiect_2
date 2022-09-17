from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/')

checkbox = chrome.find_element(By.LINK_TEXT, 'Checkbox')
sleep(2)
checkbox.click()
sleep(2)

back = chrome.find_element(By.ID, 'logo')
sleep(2)
back.click()
sleep(2)


drag_and_drop = chrome.find_element(By.LINK_TEXT, 'Drag and Drop')
sleep(2)
drag_and_drop.click()
sleep(2)

back = chrome.find_element(By.ID, 'logo')
sleep(2)
back.click()
sleep(2)

autocomplete= chrome.find_element(By.LINK_TEXT, 'Autocomplete')
sleep(2)
autocomplete.click()
sleep(2)

adress= chrome.find_element(By.ID, 'autocomplete')
sleep(2)
adress.send_keys('City Cluj, street 1: Crinului, no: 129A')
sleep(2)

street_1= chrome.find_element(By.ID, 'street_number')
sleep(2)
street_1.send_keys('Crinului')
sleep(2)

street_2= chrome.find_element(By.ID, 'route')
sleep(2)
street_2.send_keys('129A')
sleep(2)

locality= chrome.find_element(By.ID, 'locality')
sleep(2)
locality.send_keys('Cluj')
sleep(2)

state= chrome.find_element(By.ID, 'administrative_area_level_1')
sleep(2)
state.send_keys('RO')
sleep(2)

zip_code= chrome.find_element(By.ID, 'postal_code')
sleep(2)
zip_code.send_keys('12345')
sleep(2)

country= chrome.find_element(By.ID, 'country')
sleep(2)
country.send_keys('RO')
sleep(2)

chrome.quit()