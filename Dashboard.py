from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver: WebDriver=webdriver.Edge(service=serv_obj)

driver.get("https://dev.learnqoch.com/login")
driver.maximize_window()

driver.find_element(By.ID, 'email').send_keys("vidyashri@dev")
driver.find_element(By.NAME, 'password').send_keys("pass@1234")
driver.find_element(By.CLASS_NAME, 'btn').click()

print(driver.title) #LearnQoch
print(driver.current_url) #https://dev.learnqoch.com/login
print(driver.page_source) #

#My_teach = driver.find_element(By.XPATH, "//span[@class='title_lebel']")
#print("Display Status", My_teach.is_displayed())

driver.find_element(By.XPATH, "//a[@title='Edit Your Profile']").click()
#Teacher_name.click() #selct Teacher name
#print("After Selecting Teacher name:",Teacher_name.is_selected())
#print("Teacher name:",Teacher_name.is_displayed())#True
#print("Teacher name enable:",Teacher_name.is_enabled())#True
#print("before Teacher selected:",Teacher_name.is_selected())#False

