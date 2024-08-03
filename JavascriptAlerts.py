from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

alert_button=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
alert_button.click()

alert=driver.switch_to.alert
alert_text=alert.text
print(alert_text)
time.sleep(1)

alert.send_keys("Hello I am Aryan")
time.sleep(2)
alert.accept()
#alert.dismiss()
time.sleep(3)