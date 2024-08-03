from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver= webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/broken_images")
driver.maximize_window()

img=driver.find_elements(By.TAG_NAME,"img")

broken_img=[]

broken_count=0

for i in img:
    src=i.get_attribute("src")
    if src:
        response=requests.get(src)
        if response.status_code != 200:
            broken_img.append(src)
            broken_count+=1
            
print(f"{broken_count} Broken Image Found")

if broken_img:
    print("List of broken images")
    for brokeimg in broken_img:
        print(brokeimg)

else:
    print("No broken images found")
