# from telnetlib import EC
import time

import keyboard
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import executed_conditions as EC



# from selenium.webdriver.support import wait

from selenium_web.webpages.sending_keys_events import send_keys_to_element


def main():
    driver = webdriver.Firefox(executable_path=r"C:\Users\Michael Alabi\Testify Test Automation Class\WEBDRIVERS\geckodriver_win64/geckodriver.exe")
    driver.get("http://www.google.com")
    time.sleep(5)
    send_keys_to_element(driver.find_element(By.CLASS_NAME, "gLFyf"), "Python")
    keyboard.press_and_release('enter')
    time.sleep(10)
    # wikipedia_python_text = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[11]/div[2]/div/div/div[2]/div/div[5]/div/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div')
    wikipedia_python_text = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[11]/div[2]/div/div/div[2]/div/div[5]/div/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div')
    print("Wikipedia Brief:", wikipedia_python_text, wikipedia_python_text.text)
    # time.sleep(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input' ))).send_keys(send_keys_to_element("Python"))/
    # time.sleep(EC.presence_of_element_located(
    #     (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'))).send_keys(Keys.ENTER)
    #
    time.sleep(10)

    # sleep(2000)

    driver.close()

main()
