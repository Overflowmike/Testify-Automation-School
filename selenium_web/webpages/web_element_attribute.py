import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def print_element_attributes(element):
    print("ID:", element.get_attribute("id"))
    print("Class:", element.get_attribute("class"))
    print("Style:", element.get_attribute("style"))
    print("Inner Text:", element.get_attribute("innerText"))
    print("Inner HTML", element.get_attribute("innerHTML"))


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    # academy_link = driver.find_element(By.LINK_TEXT, "Academy")
    academy_link = driver.find_element(By.TAG_NAME, "form")
    print_element_attributes(academy_link)


if __name__ == '__main__':
    main()