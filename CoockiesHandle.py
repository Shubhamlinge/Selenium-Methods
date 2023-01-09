from selenium import webdriver
import time
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver = WebDriver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.learnqoch.com/")
driver.maximize_window()
#capture cookies from browser

cookies=driver.get_cookies()
print("Size of cookies:-",len(cookies))

#print details of all cookies created by browser
#for c in cookies:
#    print(c)
#print one of the values in cookies
#for c in cookies:
#    print(c.get('name'))
#add new cookies to browser
driver.add_cookie({"name":"MyCookies", "value":"1234"})
cookies=driver.get_cookies()
print("size of cookies after adding new:", len(cookies))
#delete the specific cookies from browser
driver.delete_cookie("MyCookies")
cookies=driver.get_cookies()
print("size of cookie after deleting:",len(cookies))
