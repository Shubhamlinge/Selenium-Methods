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

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"India").click()
drpcountry = Select(drp_country_ele)

#select Option from dropdown
drpcountry.select_by_visible_text("India")
#drpcountry.select_by_index("10")
#drpcountry.select_by_value("212")

alloptions=drpcountry.options
print("total number of options:", len(alloptions))

for opt in alloptions:
    print(opt.text)
#Testautomationpractice
