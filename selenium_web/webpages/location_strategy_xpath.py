import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def locate_by_xpath(driver):
    form = driver.find_element(By.XPATH, "//form[1]")
    print("Form:", form)
    form_by_full_xpath = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div[1]/div[2]/form/div[1]/div[1]/input')
    print("Form by Full XPath:", form_by_full_xpath, form_by_full_xpath.text)

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    locate_by_xpath(driver)



if __name__ == '__main__':
    main()