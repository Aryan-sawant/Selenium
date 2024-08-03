from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/nested_frames")

driver.switch_to.frame("frame-top")

driver.switch_to.frame("frame-middle")

content=driver.find_element(By.ID,"content").text
print(f"The frame is {content}")

driver.switch_to.default_content()
driver.switch_to.frame("frame-bottom")

content=driver.find_element(By.TAG_NAME,"body").text
print(f"The frame is {content}")


