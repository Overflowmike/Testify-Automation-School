
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller

def main():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get("http://www.google.org")
    driver.close()

main()