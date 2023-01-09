from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver=WebDriver=webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()

driver.switch_to.frame("iframeResult") #switch to frame

field1=driver.find_element(By.XPATH,"//input[@id='field1']")
field1.clear()
field1.send_keys("welcome shubham")
button=driver.find_element(By.XPATH,"(//button[normalize-space()='Copy Text'])")
act=ActionChains(driver)
act.double_click(button) #double click option on element
#####FFFFFAAAIIILLLLLL


