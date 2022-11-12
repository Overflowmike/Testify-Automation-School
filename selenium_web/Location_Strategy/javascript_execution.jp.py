import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    # driver.execute_script("alert('Hello World');")
    driver.execute_script("""
        const forms = document.getElementsByTagName('form');
        for (const form of forms)
            form.style.backgroundColor = 'green';
    """)
    driver.execute_script("""
        const links = document.getElementsByTagName('a');
        for (const link of form)
            link.style.color = 'red';
    """)
    time.sleep(10)


if __name__ == '__main__':
    main()

