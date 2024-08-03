from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://aryan-sawant.github.io/Aryan_Sawant.github.io/")

viewports=[(1024,768),(768,1024),(375,667),(414,896)]

for w,h in viewports:
    driver.set_window_size(w,h)
    time.sleep(5)

driver.close()

