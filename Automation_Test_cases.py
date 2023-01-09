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
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.ID, 'user-name').send_keys("standard_user")
driver.find_element(By.ID, 'password').send_keys("secret_sauce")
driver.find_element(By.ID, 'login-button').click()
time.sleep(10)

expected_text= driver.find_element(By.LINK_TEXT,"Products")
actual_text = driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/span").text
assert expected_text == actual_text, f"Error. Expected text {expected_text}"
