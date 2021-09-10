# import webdriver
from selenium import webdriver
import time

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.youtube.com")

# get element
element = driver.find_element_by_id("search")

# send keys
element.send_keys("let her go")

button = driver.find_element_by_id("search-icon-legacy")

button.click()

delay = 5
timeout = 5

element2 = driver.find_element_by_id("video-title")

element2.click()

time.sleep(100)



