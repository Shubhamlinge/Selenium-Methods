#we need to install requests in interpreter

import requests as requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

allLinks=driver.find_elements(By.TAG_NAME,"a")
count=0

for link in allLinks:
    url=link.get_attribute('href')
    try:
     res=requests.head(url)
    except:
        None

    if res.status_code>=400:
        print(url,"Broken Link")
        count+=1
    else:
        print(url,'Valid Link')

print("Total number of broken links:",count)
