
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def locate_by_class_name(driver):
    explore_course_element = driver.find_element(By.CLASS_NAME, "style_button__n7VkW")
    print("Explore Course Element:", explore_course_element)

def locate_by_text(driver):
    subscribe_text = driver.find_element(By.CSS_SELECTOR, '#__next > main > section.relative.bg-\[\#FCFCFC\].dark\:bg-\[\#013069\].pt-16.md\:pt-20.lg\:pt-28.pb-24.md\:pb-28.lg\:pb-32.xl\:pb-36 > div > div > div.w-full.md\:w-5\/12.xl\:w-4\/12 > h2')
    print("Subscribe_text:", subscribe_text, "Subscribe to receive training updates from Testify")

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com")
    locate_by_class_name(driver)
    locate_by_text(driver)

if __name__ == '__main__':
    main()















