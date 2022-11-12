import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def print_element_text(element):
    print("Text:", element.text)
# def print_element_properties(element):
#     print("Checked State:", element.get_property("checked"))
def print_attributes(element):
    print("Inner Text:", element.get_attribute("innerText"))
    print("Class:", element.get_attribute("class"))
def print_element_properties(element):
    print("Checked State:", element.get_property("checked"))
def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com")
    # academy_link = driver.find_element(By.TAG_NAME, "div")
    # print_attributes(academy_link)
    element = driver.find_element(By.CLASS_NAME, "text-white.text-xs.order-3")
    print_element_text(element)
    print_attributes(element)
    print_element_properties(element)

if __name__ == '__main__':
    main()
