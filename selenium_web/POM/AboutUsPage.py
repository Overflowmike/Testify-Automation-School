
from selenium.webdriver.common.by import By


class AboutUsPage:
    def __init__(self, driver):
        driver.get("https://www.testifyltd.com/about")
        self.title = driver.find_element(By.TAG_NAME, 'h1')