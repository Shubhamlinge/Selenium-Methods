from selenium import webdriver
import time
from day24 import XlUtils
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

serv_obj = Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
driver = WebDriver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file="C:\\data\\caldata.xlsx"
rows=XlUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    #reading data from rows
    pric=XlUtils.readData(file,"Sheet1",r,1)#20000
    rateofintrest = XlUtils.readData(file, "Sheet1", r, 2)
    per1 = XlUtils.readData(file, "Sheet1", r, 3)
    per2 = XlUtils.readData(file, "Sheet1", r, 4)
    fre = XlUtils.readData(file, "Sheet1", r, 5)
    exp_mvalue = XlUtils.readData(file, "Sheet1", r, 6)
    #passing data to application
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH,"// input[ @ id = 'interest']").send_keys(rateofintrest)
    driver.find_element(By.XPATH,"// input[ @ id = 'tenure']").send_keys(per1)
    #select dropdown value
    perioddrp=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(per2)
    #select frequency dropdown
    frequencydrp=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    frequencydrp.select_by_visible_text(fre)
    #select calculate button
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    act_mvalue=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

    #validation
    if float(exp_mvalue)==float(act_mvalue):
        print("test passed")
        XlUtils.writeData(file,"Sheet1",r,8,"Passed")
        XlUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test failed")
        XlUtils.writeData(file,"Sheet1",r,8,"Failed")
        XlUtils.fillRedColor(file,"Sheet1",r,8)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(3)

driver.close()

