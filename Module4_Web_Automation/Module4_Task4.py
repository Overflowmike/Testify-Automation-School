import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_element(element, *keys):
    element.send_keys(keys)

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    send_keys_to_element(driver.find_element(By.NAME, "email"), "princefamous01@yahoo.com")
    time.sleep(2)
    send_keys_to_element(driver.find_element(By.NAME, "pass"), "XXXXXXXX")
    time.sleep(3)
    log_in_button = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/button[1]')
    log_in_button.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/button[1]").click()
    time.sleep(15)



if __name__ == '__main__':
    main()


