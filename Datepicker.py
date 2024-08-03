from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime,timedelta

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/datepicker/")

driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']").click()
framelo=driver.find_element(By.XPATH,"//iframe[@class='demo-frame lazyloaded']")
driver.switch_to.frame(framelo)
time.sleep(3)

datepick=driver.find_element(By.CSS_SELECTOR,"#datepicker").click()

current_date= datetime.now()
next_date= current_date + timedelta(days=-2)
formatted_date=next_date.strftime("%d/%m/%y")
driver.find_element(By.CSS_SELECTOR,"#datepicker").send_keys(formatted_date + Keys.TAB)
time.sleep(5)
driver.quit()