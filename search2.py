from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.youtube.com/results?search_query=let+her+go")

user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for i in user_data:
    links.append(i.get_attribute('href'))
print(links)

wait = WebDriverWait(driver, 10)
for x in links:
 driver.get(x)
 v_title =wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.title.style-scope.ytd-video-primary-info-renderer"))).text
 v_name = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id=”text”]/a'))).text
 v_likes = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id=”text”]'))).text
 v_dlikes= wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id=”top-level-buttons”]/ytd-toggle-button-renderer[2]/a'))).text
 v_views= wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id=”count”]/yt-view-count-renderer/span[1]'))).text
 
 print(v_title)
 print(v_name)
 print(v_likes)
 print(v_dlikes)
 print(v_views)