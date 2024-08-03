from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")

driver.find_element(By.XPATH,"(//input[@type='checkbox'])[1]").click()
time.sleep(5)
driver.close()