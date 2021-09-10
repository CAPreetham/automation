# import webdriver
from selenium import webdriver
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

button = driver.find_element_by_id ("search-icon-legacy")

button.click()

button2 =driver.find_element_by_class_name("yt-simple-endpoint style-scope ytd-button-renderer").click()