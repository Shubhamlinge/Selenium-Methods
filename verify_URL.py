from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver: WebDriver=webdriver.Edge(service=serv_obj)

driver.get("https://dev.learnqoch.com/login")
driver.maximize_window()

print(driver.title) #LearnQoch
print(driver.current_url) #https://dev.learnqoch.com/login
print(driver.page_source) #

driver.quit()