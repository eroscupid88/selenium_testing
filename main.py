import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
os.environ['PATH'] += r":/Users/dillonvu/chromeDriver"
path = os.environ['PATH']
print(path)
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('http://localhost:3000/register')

firstname = driver.find_element(By.NAME, 'firstname')
lastname = driver.find_element(By.NAME, 'lastname')
registeremail = driver.find_element(By.NAME, 'email')
registerpassword = driver.find_element(By.NAME, 'password')
registerpassword1 = driver.find_element(By.NAME, 'password2')
registerbtn = driver.find_element(By.CLASS_NAME, 'btn')

firstname.send_keys('Dillon')
lastname.send_keys('Vu')
registeremail.send_keys('a@yahoo.com')
registerpassword.send_keys('123456')
registerpassword1.send_keys('123456')

registerbtn.click()
email_input = driver.find_element(By.NAME, 'email')
password_input = driver.find_element(By.NAME, 'password')

email_input.send_keys('a@yahoo.com')
password_input.send_keys('123456')

btn = driver.find_element(By.CLASS_NAME, 'btn')
btn.click()
