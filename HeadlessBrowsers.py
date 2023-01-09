from selenium import webdriver

def headless_edge():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:\\Users\\Admin\\Downloads\\Driver\\msedgedriver.exe")
    ops=webdriver.EdgeOptions()
    ops.headless=True
    driver=webdriver.Edge(service=serv_obj,options=ops)
    return driver

driver=headless_edge()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()