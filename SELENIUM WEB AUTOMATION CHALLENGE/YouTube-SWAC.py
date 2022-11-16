import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.youtube.com/watch?v=6RkRsnNT09c")
    time.sleep(5)
    youTube_play_button = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[33]/div[2]/div[1]/button')
    youTube_play_button.click()
    time.sleep(5)
    first_comment = driver.find_element(By.XPATH, '//*[@id="content-text"]/span')
    print("First Comment:", first_comment, first_comment.text)
    time.sleep(5)
    second_comment = driver.find_element(By.XPATH, '//*[@id="content-text"]')
    print("Second Comment:", second_comment.text)
    time.sleep(5)
    driver.close()




if __name__ == '__main__':
        main()