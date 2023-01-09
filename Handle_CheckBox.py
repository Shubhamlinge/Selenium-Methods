import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver: WebDriver=webdriver.Edge(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
#select specific checkbox
#driver.find_element(By.XPATH,"//input[@id='monday']").click()

#select all Checkboxex
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

#approach 1
#for i in range(len(checkboxes)):
 #   checkboxes[i].click()

#approach 2
#for checkbox in checkboxes:
#    checkbox.click()

#3)Select Multiple checkbox by choice

#for checkbox in checkboxes:
#    weekname=checkbox.get_attribute('id')
#    if weekname=='monday'or weekname=='sunday':
#        checkbox.click()

#4)Select last two checkbox
#range(5,7)-->6,7
#total number of element-2=starting index
#for i in range(len(checkboxes)-2,len(checkboxes)):
#    checkboxes[i].click()

#5)Select first two checkbox

#for i in range(len(checkboxes)):
#    if i<2:
#        checkboxes[i].click()
#time.sleep(2)
#6 Clearing all the checkboxes
#for checkbox in checkboxes:
#    if checkbox.is_selected():
#        checkbox.click()