from selenium import webdriver
import time
from day24 import XlUtils
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

serv_obj = Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver = WebDriver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

file="C:\\data\\datalogin.xlsx"
rows=XlUtils.getRowCount(file,"Sheet1")

for r in range(3,rows+1):
    #read data
    user=XlUtils.readData(file,"Sheet1",r,1)
    pas=XlUtils.readData(file,"Sheet1",r,2)
    exp_value=XlUtils.readData(file,"Sheet1",r,3)
    #passing data to application
    driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys(user)
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys(pas)
    driver.find_element(By.XPATH,"//input[@id='login-button']").click()
    time.sleep(3)
    act_value = driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack").text
    driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']").click()
    driver.find_element(By.XPATH,"//a[@id='logout_sidebar_link']").click()

    #validations
    if int(act_value) == int(exp_value):
        print("test passed")
        XlUtils.writeData(file,"Sheet1",r,4,"Passed")
        XlUtils.fillGreenColor(file,"Sheet1",r,4)
    else:
        print("test failed")
        XlUtils.writeData(file, "Sheet1", r, 4, "Failed")
        XlUtils.fillRedColor(file, "Sheet1", r, 4)
    driver.find_element(By.XPATH,"//input[@id='user-name']").clear()
    driver.find_element(By.XPATH, "//input[@id='password']").clear()
    time.sleep()
driver.close()