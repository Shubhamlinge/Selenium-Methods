from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver: WebDriver=webdriver.Edge(service=serv_obj)

driver.get("https://www.learnqoch.com/")
driver.maximize_window()

#is_displayed #is_enabled
LgnBtn=driver.find_element(By.XPATH,"//a[normalize-space()='Log In']")

print("Display Status:", LgnBtn.is_displayed())
print("Display Status:", LgnBtn.is_enabled())

radio_btn=driver.find_element(By.XPATH,"//input[@value='Parent']")

print("Radio Working:",radio_btn.is_selected())
