import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_element(element, *keys):
    element.send_keys(keys)

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    send_keys_to_element(driver.find_element(By.NAME, "firstname"), "Michael")
    send_keys_to_element(driver.find_element(By.NAME, "lastname"), "Flow")
    send_keys_to_element(driver.find_element(By.NAME, "email"), "hello@testify.com")
    send_keys_to_element(driver.find_element(By.NAME, "message"), "Hello From Test Automation class")
    form = driver.find_element(By.TAG_NAME, "form")
    form.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div[1]/div[2]/form/div[3]/div/div[1]/label').click()
    form.find_element(By.TAG_NAME, "button").click()
    time.sleep(15)



if __name__ == '__main__':
    main()


