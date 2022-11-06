from time import sleep

from selenium import webdriver

def main():
    driver = webdriver.Firefox(executable_path=r"C:\Users\Michael Alabi\Testify Test Automation Class\WEBDRIVERS\geckodriver_win64/geckodriver.exe")
    driver.get("http://www.google.com")
    # sleep(2000)
    driver.close()

main()
