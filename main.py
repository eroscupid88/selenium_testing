import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
os.environ['PATH'] += r":/Users/dillonvu/chromeDriver"
path = os.environ['PATH']
print(path)
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('http://automationpractice.com/index.php')


WebDriverWait(driver, 30).until(
    # condition
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'shopping_cart'),  # element filtration

        'Cart (empty)'  # the expected text
    )
)
