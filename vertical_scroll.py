from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver = WebDriver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#1.Scroll down page by pixel
#driver.execute_script("window.scrollBy(0,3000)","")
#value=driver.execute_script("return window.pageYOffset;")
#print("Number of pixels moved:",value)#3000
#2.Scroll down page till the element is visible
flag=driver.find_element(By.XPATH,"// img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)
