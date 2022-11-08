import time
from Task5_STST import Task5_STST
from Task5_TAS import Task5_TAS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    test_automation_simplified = Task5_TAS(driver)
    print(test_automation_simplified.title.text)
    switch_to_testing = Task5_STST(driver)
    print(switch_to_testing.title.text)
    # print(switch_to_testing.firstname_input, switch_to_testing.lastname_input)
    # contact_page.submit_button.click()
    time.sleep(20)



if __name__ == '__main__':
    main()
