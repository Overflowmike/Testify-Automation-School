from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#
# def locate_by_id(driver):
#     email_element = driver.find_element(By.ID, "email")
#     print("Email Element:", email_element)
#     password_element = driver.find_element(By.ID, "pass")
#     print("Password Element:", password_element)
#
#
# def locate_by_name(driver):
#     firstname_element = driver.find_element(By.NAME, "firstname")
#     print("Firstname Element:", firstname_element)
#     lastname_element = driver.find_element(By.NAME, "lastname")
#     print("Lastname Element:", lastname_element)


def locate_by_class_name(driver):
    explore_course_element = driver.find_element(By.CLASS_NAME, "style_button__n7VkW")
    print("Explore Course Element:", explore_course_element)

    # rr_elements = driver.find_elements(By.CLASS_NAME, "react-reveal")
    # for rr_elements in rr_elements:
    #     print("React Reveal Element:", rr_elements)


def main():
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.get("https://facebook.com")
    # locate_by_id(driver)


    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.get("https://www.testifyltd.com/contact")
    # locate_by_name(driver)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com")
    locate_by_class_name(driver)


if __name__ == '__main__':
    main()