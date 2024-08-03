from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
#Implicit wait means it will wait maximum for particular event dynamically 
#for a provided value and if the event takes less time to execute then it will get executed fastly and not wait for implicit wait value
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.saucedemo.com/v1/index.html")
    
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click() 
driver.find_element(By.XPATH,"//button[normalize-space()='Open Menu']").click()
driver.find_element(By.XPATH,"//a[@id='logout_sidebar_link']").click()

driver.quit()




