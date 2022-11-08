import time
from ContactPage import ContactPage
from AboutUsPage import AboutUsPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # about_us_page = AboutUsPage(driver)
    # print(about_us_page.title.text)
    contact_page = ContactPage(driver)
    print(contact_page.firstname_input, contact_page.lastname_input)
    contact_page.submit_button.click()
    time.sleep(20)



if __name__ == '__main__':
    main()
