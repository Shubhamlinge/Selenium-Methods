from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver = WebDriver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='select2-billing_country-container']").click()
driver.find_element(By.XPATH,"")