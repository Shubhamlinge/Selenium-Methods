import time
from _ast import Assert

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\geckodriver.exe")
driver: WebDriver=webdriver.Firefox(service=serv_obj)
driver.implicitly_wait(5)
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm#")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[normalize-space()='Button']").click()

/html/body/main/div/div/div[2]/div[6]/div/form/table/tbody/tr[11]/td[2]/button