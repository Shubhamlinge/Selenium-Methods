import time

from select import select
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver: WebDriver=webdriver.Edge(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"(//button[normalize-space()='Click for JS Prompt'])[1]").click()
time.sleep(5)
alertwindow=driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("welcome")
alertwindow.accept()
#alertwindow.dismiss()