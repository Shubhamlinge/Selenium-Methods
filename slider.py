from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver = WebDriver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slide = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
max_slide = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")



act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slide, 100, 0).perform() #{'x': 161, 'y': 250}
act.drag_and_drop_by_offset(max_slide, -39, 0).perform()#{'x': 506, 'y': 250}

print("Location of slider before moving")
print(min_slide.location)  # {'x': 59, 'y': 250}
print(max_slide.location)  # {'x': 545, 'y': 250}