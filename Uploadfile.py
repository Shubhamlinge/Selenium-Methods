from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver = WebDriver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.monsterindia.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@class='btn block resume-btn btn-orange mt20']").click()
driver.find_element(By.XPATH,"//*[@id='file-upload']").send_keys("C:\mindqoach\Shubham SAP 5 years-1.pdf")
