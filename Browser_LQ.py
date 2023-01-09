import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver: WebDriver=webdriver.Edge(service=serv_obj)

driver.get("https://www.learnqoch.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Coding").click()

time.sleep(5)
#driver.close()
driver.quit()

