import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Python Automation to get YouTube Subtitle
def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.youtube.com/watch?v=WhJdOB7Wv0s")
    youTube_play_button = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[35]/div[2]/div[1]/button')
    youTube_play_button.click()
    time.sleep(10)
    first_comment = driver.find_element(By.CLASS_NAME, "ytp-caption-segment")
    print("First Comment:", first_comment.text)
    time.sleep(2)
    second_comment = driver.find_element(By.CLASS_NAME, "ytp-caption-segment")
    print("Second Comment:", second_comment.text)
    time.sleep(7)
    driver.close()







if __name__ == '__main__':
        main()
