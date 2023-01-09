from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver=WebDriver=webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
act=ActionChains(driver)
act.context_click(button).perform()


