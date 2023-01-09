import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

serv_obj=Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver: WebDriver=webdriver.Edge(service=serv_obj)
driver.implicitly_wait(5)
driver.get("https://dev.learnqoch.com/login")
driver.maximize_window()

driver.find_element(By.ID, 'email').send_keys("vidyashri@dev")
driver.find_element(By.NAME, 'password').send_keys("pass@1234")
driver.find_element(By.CLASS_NAME, 'btn').click()
time.sleep(10)
driver.find_element(By.LINK_TEXT,"Assessment").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[@class='add_que_assessment_label']").click()
driver.find_element(By.ID,"title").send_keys("Mixed Automated assessment")

select = Select(driver.find_element(By.ID,"grade"))
select.select_by_visible_text("Class-12")

select = Select(driver.find_element(By.ID,"grade_division_id"))
select.select_by_visible_text("Morning Shift")
time.sleep(2)
select = Select(driver.find_element(By.ID,"subject_id"))
select.select_by_visible_text("Maths")
time.sleep(2)
select = Select(driver.find_element(By.ID,"chapter_id"))
select.select_by_visible_text("Real Numbers")

#select = Select(driver.find_element(By.ID,"test_category"))
#select.select_by_visible_text("Mixed")
time.sleep(1)
driver.find_element(By.ID,"get_question_btn").click()
time.sleep(3)

driver.find_element(By.NAME,'test_duration').send_keys("10")
time.sleep(2)
all_que=driver.find_elements(By.XPATH,'//input[@class="test_type_chkbox quest_type_chkbox"]')
print(len(all_que))
for all_question in all_que:
    print(all_question)

#driver.find_element(By.ID,"submit_test_btn").click()
#time.sleep(2)
#my_alert=driver.switch_to.alert
#my_alert.accept()

driver.close()
