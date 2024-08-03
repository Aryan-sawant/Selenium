from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,700)")

table = driver.find_element(By.ID,"countries")
rows=driver.find_elements(By.TAG_NAME,"tr")
print(len(rows)-1)

target="Inia"
found=False
for r in rows:
    cells=r.find_elements(By.TAG_NAME,"td")
    for c in cells:
        if target == c.text:
            print(f"{c.text} Found!")
            found= True    
    if found:
        break
if not found:  
    print("Target not found")
        
        


time.sleep(3)