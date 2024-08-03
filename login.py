from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

driver = webdriver.Chrome()
driver.maximize_window()

# List of usernames
names = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]
password = "secret_sauce"

url = "https://www.saucedemo.com/v1/"
driver.get(url)

# Select a random username from the list
random_name = random.choice(names)

# Find the username and password fields
name_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")

# Enter the random username and password
name_field.send_keys(random_name)
password_field.send_keys(password)

# Find and click the login button
login_button = driver.find_element(By.ID, "login-button")

assert not login_button.get_attribute("disabled")

login_button.click()

# Wait for the page to load
time.sleep(3)

# Check for successful login
try:
    success_login = driver.find_element(By.CSS_SELECTOR, ".product_label")
    assert success_login.text == "Products"
    print(f"Login successful with user: {random_name}")
except Exception as e:
    print(f"Login failed for user: {random_name}. Error: {e}")

# Close the browser
driver.quit()
