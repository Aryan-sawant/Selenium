from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
import time

# Replace with the path to your ChromeDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Replace with the URL of your Google Form
url = "https://docs.google.com/forms/d/e/1FAIpQLSeozJH76O8pz_h59LIe4QFKaBfKPlOrZhc2_Jeyl4zrJeeYWQ/viewform"
driver.get(url)

# Wait for the form to load
time.sleep(3)

try:
    # Fill in the 'Name' field
    name_field = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
    name_field.send_keys("Aryan Sawant")
except NoSuchElementException:
    print("Name field not found")
    driver.quit()
    exit()

try:
    # Fill in the 'Email' field
    email_field = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
    email_field.send_keys("aryansawant123@gmail.com")
except NoSuchElementException:
    print("Email field not found")
    driver.quit()
    exit()

try:
    # Fill in the 'Subject' field
    subject_field = driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
    subject_field.send_keys("Selenium Tutorial")
except NoSuchElementException:
    print("Subject field not found")
    driver.quit()
    exit()

try:
    # Fill in the 'Message' field
    message_field = driver.find_element(By.XPATH, "//textarea[@aria-label='Your answer']")
    message_field.send_keys("Happily learning selenium")
except NoSuchElementException:
    print("Message field not found")
    driver.quit()
    exit()

# Wait for a moment to ensure all fields are filled
time.sleep(1)

try:
    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//span[contains(text(),'Submit')]")
    submit_button.click()
except NoSuchElementException:
    print("Submit button not found")
    driver.quit()
    exit()
except ElementClickInterceptedException:
    print("Submit button click intercepted")
    driver.quit()
    exit()

# Wait to ensure the form is submitted
time.sleep(3)

# Close the browser
driver.quit()
