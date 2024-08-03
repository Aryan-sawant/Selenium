from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver= webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME,"a")
print(f"Total links {len(all_links)}")

broken_link_count=0

for link in all_links:
    href=link.get_attribute('href')
    response=requests.get(href)

    if response.status_code>400:
        print(f"Broken Link : {href} {response.status_code} Error")
        broken_link_count += 1

print(f"{broken_link_count} Broken Link Found!")
driver.quit()