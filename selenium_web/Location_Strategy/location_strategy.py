
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com")
    hero_element = driver.find_element(By.XPATH, "/html/body/div/main/section[1]/div/div[1]/div[1]/h1")
    print("Hero Element", hero_element, hero_element.text)

    # Links = driver.find_elements(By.TAG_NAME, "a")
    # for Link in Links:
    #     print("link:", Link.text)


if __name__ == '__main__':
    main()