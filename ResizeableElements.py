from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Resizable.html")

resizeable_element=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
intitial_element_size=driver.find_element(By.XPATH,"//div[@id='resizable']")
initial_size=intitial_element_size.size
print(initial_size)
time.sleep(3)

actions = ActionChains(driver)
actions.click_and_hold(resizeable_element).move_by_offset(100,100).release().perform()
time.sleep(3)

resized_element=intitial_element_size.size
print(resized_element)
driver.quit()
