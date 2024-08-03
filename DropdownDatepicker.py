from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from datetime import datetime,timedelta

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.find_element(By.ID,"datepicker2").click()
time.sleep(2)

current_date=datetime.now()
print(current_date)

next_day = current_date + timedelta(days=1)
Next_day=(str(next_day.day))

current_month=datetime.now().month
current_year=datetime.now().year

next_month=(current_month % 12) + 1
next_month_year=f"{next_month}/{current_year}"

month_dropdown=driver.find_element(By.CSS_SELECTOR,"select[title='Change the month']")
select=Select(month_dropdown)
select.select_by_value(str(next_month_year))

year_dropdown=driver.find_element(By.CSS_SELECTOR,"select[title='Change the year']")
selectyear=Select(year_dropdown)
selectyear.select_by_visible_text("2024")
driver.find_element(By.LINK_TEXT,Next_day).click()
time.sleep(3)