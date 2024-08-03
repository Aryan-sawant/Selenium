from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://aryan-sawant.github.io/Aryan_Sawant.github.io/")
browser.maximize_window()
title = browser.title
print(title)