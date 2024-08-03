from selenium import webdriver
import time

username="admin"
password="admin"

driver= webdriver.Chrome()
driver.maximize_window()

# Syntax for authentication : https://username:password@domain/path
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)

