from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.maximize_window()
driver.switch_to.new_window()
driver.get("https://aryan-sawant.github.io/Aryan_Sawant.github.io/")
time.sleep(5)

number_of_tab= len(driver.window_handles)
print(f"There are {number_of_tab} tabs")

tabs_value=driver.window_handles
print(tabs_value)

current_tab_value=driver.current_window_handle
print(current_tab_value)

driver.find_element(By.XPATH,"(//a[@class='btn btn-white btn-outline-white py-3 px-4'][normalize-space()='GitHub'])[3]").click()
time.sleep(5)

firstab=driver.window_handles[0]
if current_tab_value != firstab:
    driver.switch_to.window(firstab)

driver.find_element(By.CSS_SELECTOR,"a[href='https://contribute.jquery.org/']").click()
time.sleep(3)
