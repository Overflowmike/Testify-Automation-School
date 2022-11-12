
from selenium.webdriver.common.by import By


class Task5_STST:

    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/switch-to-software-testing")
        self.title = driver.find_element(By.TAG_NAME, 'h1')
        # self.email_input = driver.find_element(By.NAME, 'email')
        # self.message_input = driver.find_element(By.NAME, 'message')
        # self.lastname_input = driver.find_element(By.NAME, 'lastname')
        # self.firstname_input = driver.find_element(By.NAME, 'firstname')
        # self.submit_button = driver.find_element(By.TAG_NAME, 'form').find_element(By.TAG_NAME, 'button')
