from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://cloud.google.com")

time.sleep(2)  

button_element = driver.find_element_by_css_selector("[class*=tShh4b]")

button_element.click()

time.sleep(2) 

text_box = driver.find_element_by_id("identifierId")

text_box.send_keys("dukeanh12@gmail.com")

text_box.send_keys(Keys.ENTER)

time.sleep(2) 

text_box = driver.find_element_by_css_selector("[class*=whsOnd zHQkBf]")

text_box.send_keys("demopassword")

text_box.send_keys(Keys.ENTER)

driver.get("https://cloud.google.com")

time.sleep(2)  

button_element = driver.find_element_by_css_selector("[jsname='Ohx1pb']")

button_element.click()

text_box = driver.find_element_by_css_selector("[jsname='YPqjbf']")

text_box.send_keys("google")

driver.quit()
