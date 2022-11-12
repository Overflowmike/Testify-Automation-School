import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://weather.com/")
    time.sleep(5)
    current_temperature = driver.find_element(By.CLASS_NAME, "CurrentConditions--tempValue--MHmYY")
    time.sleep(5)
    print("Current Temperature:", current_temperature, current_temperature.text)
    time.sleep(10)
    driver.close()


if __name__ == '__main__':
    main()
