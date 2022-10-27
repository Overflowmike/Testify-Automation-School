from time import sleep

from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path="C:/Users/Michael Alabi/Testify Test Automation Class/WEBDRIVERS/chromedriver_win32/chromedriver")
    driver.get("http://www.google.com")
    sleep(2000)
    driver.close()

main()
