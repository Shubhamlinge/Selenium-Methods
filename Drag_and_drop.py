from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver=WebDriver=webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

sourse_ele=driver.find_element(By.ID,"box6")
targt=driver.find_element(By.ID,"box106")
act=ActionChains(driver)
act.drag_and_drop(sourse_ele,targt).perform() #drag and drop operation
