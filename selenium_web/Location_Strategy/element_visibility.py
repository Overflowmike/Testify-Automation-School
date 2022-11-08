import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    form = driver.find_element(By.TAG_NAME, 'form')
    print("Form States:", form.is_displayed(), form.is_enabled())
    submit_button = form.find_element(By.TAG_NAME, 'button')
    print("Submit Button States:", submit_button.is_displayed(), submit_button.is_enabled())
    if submit_button.is_displayed():
        print("Clicking 1")
        submit_button.click()
        time.sleep(5)
    # driver.maximize_window()
    print("Submit Button States:", submit_button.is_displayed(), submit_button.is_enabled())
    if submit_button.is_displayed():
        print("Clicking 2")
        submit_button.click()
    time.sleep(15)



if __name__ == '__main__':
    main()