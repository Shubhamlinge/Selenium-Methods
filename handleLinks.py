import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver: WebDriver = webdriver.Edge(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

# find the number of links on the page
links= driver.find_element(By.TAG_NAME, 'a')
print("total number of links:", links)

for link in links:
    print(link)
