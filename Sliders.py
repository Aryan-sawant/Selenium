from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/horizontal_slider")

slider=driver.find_element(By.XPATH,"//input[@type='range']")

actions=ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(50,0).release().perform()
time.sleep(5)
driver.quit()