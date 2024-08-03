from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver= webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()

dropdown_element=driver.find_element(By.ID,"dropdown")

select= Select(dropdown_element)

target_option="Option 2"
for option in select.options:
    if option.text == target_option:
        option.click()
        print(f"{target_option} Found!")
    else:
        print(f"{target_option} not Found")



list_count=len(select.options)
expected_count = 4
if list_count == expected_count:
    print("Matched")
else:
    print("Mismatched")

#select.select_by_visible_text("Option 1")
#select.select_by_index(2)
#select.select_by_value("1")

time.sleep(5)
