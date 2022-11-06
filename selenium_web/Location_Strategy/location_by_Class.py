

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com")
    hero_element = driver.find_element(By.CLASS_NAME, "react-reveal")
    print("Hero Element", hero_element, hero_element.text)


if __name__ == '__main__':
    main()















