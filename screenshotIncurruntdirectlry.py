from selenium import webdriver
import time
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver = WebDriver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#driver.save_screenshot(os.getcwd()+"webpageScreenshot.png")
driver.get_screenshot_as_file(os.getcwd()+"webpageScreenshot.png")
driver.get_screenshot_as_base64()
driver.close()