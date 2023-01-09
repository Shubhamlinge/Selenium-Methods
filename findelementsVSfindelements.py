import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver: WebDriver=webdriver.Edge(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
### find_element() -Return Single Element

#1)Locators Matching with single webelement
#element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
#element.send_keys("Laptop")

#2)Locators Matching With Multiple Webelements
#element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
#print(element.text)

#3)Element not available then throw NosuchElementExceptions
login_element=driver.find_element(By.LINK_TEXT,"Log in")
login_element.click()

###### find_elements() - return multiple web elements
#1) Locators Matching with single webelements
#elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
#print(len(elements)) #1
#elements[0].send_keys("apple macbook")

#2) Locators Matching with multiple Webelements
elements=driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(len(elements)) #23
#print(elements[0].text) #sitemap

#for ele in elements:
#    print(ele.text)

