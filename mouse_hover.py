from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver=WebDriver=webdriver.Edge(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(3)

admin=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b")
usrmgm=driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']")
users=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']")

act=ActionChains(driver)

act.move_to_element(admin).move_to_element(usrmgm).move_to_element(users).click().perform()
