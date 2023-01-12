import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# FBN Web Automation Task Project

# Section A: Automate Login Test For Sauce-Demo Website

def send_keys_to_element(element, *keys):
    element.send_keys(keys)

def main():
    #Launch browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    time.sleep(4)
    # Enter Username and Password
    send_keys_to_element(driver.find_element(By.ID, "user-name"), "standard_user")
    time.sleep(2)
    send_keys_to_element(driver.find_element(By.ID, 'password'), "secret_sauce")
    time.sleep(5)
    # Log in
    log_in_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    time.sleep(3)
    log_in_button.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(5)
    driver.close()

if __name__ == '__main__':
    main()
    print("Test Pass")