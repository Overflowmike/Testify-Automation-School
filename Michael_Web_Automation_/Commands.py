from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Application commands
driver - webdriver.Chrome(service=Service(ChromeDriverManager().install))

driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.implicity_wait(5)

driver.maximize_window()

print(driver.title) # OrangeHRM --> This will give the current title page
print(driver.current_url) # "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login ---> This will give 
# the current url of the application

print(driver.page_source) # This will give the source of the code incase we need to d some HTML validations 
driver.quit()