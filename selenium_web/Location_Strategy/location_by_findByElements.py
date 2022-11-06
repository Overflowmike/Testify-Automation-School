
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com")

    # find_elements with s returns all results, without s in element returns the first result
    Links = driver.find_elements(By.TAG_NAME, "a")
    for Link in Links:
        print("link:", Link.text)


if __name__ == '__main__':
    main()