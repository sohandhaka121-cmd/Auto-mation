from selenium import webdriver
from selenium.webdriver.common.by import By  

from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(2) 
 
driver.find_element(By.NAME, "my-text").send_keys("Pythongi") 
driver.find_element(By.NAME, "my-password").send_keys("87654321") 
driver.find_element(By.NAME, "my-textarea").send_keys("Good") 
 
# dropdown 
driver.find_element(By.NAME, "my-select").send_keys("sohanur") 
driver.find_element(By.CSS_SELECTOR,"option[value='1']").click()
driver.find_element(By.NAME, "my-datalist").send_keys("spain") 
 
# checkbox 
driver.find_element(By.NAME, "my-check-2").click() 
driver.find_element(By.NAME, "my-check-2").click() 
 
#color 
driver.find_element(By.NAME, "my-colors").send_keys("#FFDEDE") 
 
# date 
driver.find_element(By.NAME, "my-date").send_keys("2013-11-06") 
 
time.sleep(5) 
 
driver.find_element(By.CSS_SELECTOR,"button").click() 
 
input("press Enter key to close") 
driver.quit()