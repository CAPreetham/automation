# import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.youtube.com")

driver.maximize_window()

# get element
element = driver.find_element_by_id("search")

# send keys
element.send_keys("let her go")

button = driver.find_element_by_id("search-icon-legacy")
button.click()



try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_element_located((By.XPATH, '//*[@id="dismissible"]'))
    )
    element.click()

finally:
    time.sleep(20)