import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver: WebDriver=webdriver.Edge(service=serv_obj)

driver.get("https://www.learnqoch.com/")
driver.get("https://dev.learnqoch.com/login")
driver.back() #offical LearnQoch
time.sleep(3)
driver.forward() #Student Login
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.quit()


#driver.maximize_window()
