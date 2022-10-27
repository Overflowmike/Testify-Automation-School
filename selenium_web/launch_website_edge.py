from time import sleep

from selenium import webdriver

def main():
    driver = webdriver.Edge(executable_path=r"C:\Users\Michael Alabi\Testify Test Automation Class\WEBDRIVERS\edgedriver_win64/msedgedriver.exe")
    driver.get("http://www.google.com")
    # sleep(2000)
    driver.close()

main()
