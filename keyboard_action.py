from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver = WebDriver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

input1.send_keys("Welcome Shubham")
act=ActionChains(driver)
#input1 ctrl A =seelcte te text

#act.key_down(Keys.CONTROL)
#act.send_keys("a")
#act.key_up(Keys.CONTROL)
#act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
#input ctl C=copy text

#act.key_down(Keys.CONTROL)
#act.send_keys("C")
#act.key_up(Keys.CONTROL)
#act.perform()

act.key_down(Keys.CONTROL).send_keys("C").key_up(Keys.CONTROL).perform()

#press TAB Tkey

act.send_keys(Keys.TAB).perform()
#input2 CTRL + v
#act.key_down(Keys.CONTROL)
#act.send_keys("v")
#act.key_up(Keys.CONTROL)
#act.perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()