from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")


iframe=driver.find_element(By.ID,"mce_0_ifr")
driver.switch_to.frame(iframe)

text_editor=driver.find_element(By.ID,"tinymce")
text_editor.clear()
text_editor.send_keys("This is Aryan!")
time.sleep(5)

driver.switch_to.default_content()
selenium_link=driver.find_element(By.XPATH,"//a[normalize-space()='Elemental Selenium']")
selenium_link.click()
