from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

#1 - XPATH: atribut=valoare

chrome.get('http://automationpractice.com/index.php')

chrome.find_element(By.XPATH, '//input[@id="search_query_top"]').send_keys('Blo')
sleep(3)
chrome.find_element(By.XPATH, '//form//input[@id="search_query_top"]').send_keys('u')
sleep(3)
chrome.find_element(By.XPATH, '//div/form/input[@id="search_query_top"]').send_keys('se')
sleep(3)

chrome.quit()

#2: XPATH: OR primul gasit dintre variante

chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')

s = chrome.find_element(By.XPATH, '//input[@id="email"] | //input[@id="passwd"]')
sleep(3)
s.send_keys('x@yahoo.com')
sleep(3)
s.clear()

chrome.quit()

#3: XPATH: * oricare respecta regula

chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')

s = chrome.find_element(By.XPATH, '//*[@id="SubmitLogin"]/span')
s.click()
sleep(2)

chrome.quit()

#4 XPATH: (xpath)[1]

chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')

chrome.find_element(By.XPATH, '(//input[@class="is_required validate account_input form-control"])[2]').send_keys('Monica@gmail.com')
chrome.find_elements(By.XPATH, '(//input[@class="is_required validate account_input form-control"])')[2].send_keys('iulie2022')

#5 XPATH: link text
chrome.get('https://formy-project.herokuapp.com/form')
chrome.find_element(By.XPATH, '//option[text()="0-1"]').click()
sleep(3)

chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.find_element(By.XPATH, '//span[text()="Years of Experience"]').click()
sleep(3)

chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.find_element(By.XPATH, '//a[text()="Click here to Download File"]').click()
sleep(3)

#6 XPATH: following-sibling

chrome.get('https://formy-project.herokuapp.com/autocomplete')
chrome.find_element(By.XPATH, '//div[@class="col-sm-8 col-sm-offset-2"]//following-sibling::div').send_keys('Strada')
chrome.quit()

#7 XPATH: parent
chrome.get('https://formy-project.herokuapp.com/autocomplete')
chrome.find_element(By.XPATH, '//div[@class="col-sm-8 col-sm-offset-2"]//parent::div').send_keys('Strada')
chrome.quit()