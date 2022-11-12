# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
#
# def locate_youTube_comment(driver):
#     comment_first_element = driver.find_element(By.ID, "content")
#     print("Comment First Element:", comment_first_element, comment_first_element.text)
#     comment_elements = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
#     for comment_elements in comment_elements:
#         print("Comment Reveal Element:", comment_elements, comment_elements.text)
# def main():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get("https://www.youtube.com/watch?v=WhJdOB7Wv0s")
#     time.sleep(5)
#     youTube_play_button = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[35]/div[2]/div[1]/button')
#     youTube_play_button.click()
#     time.sleep(5)
#     locate_youTube_comment(driver)
#
#     # first_comment = driver.find_element(By.ID, 'content')
#     # print("First Comment:", first_comment, first_comment.text)
#     # time.sleep(2)
#     # second_comment = driver.find_element(By.CSS_SELECTOR, '//*[@id="content-text"]')
#     # print("Second Comment:", second_comment.text)
#     # time.sleep(7)
#     driver.close()
#
#
# if __name__ == '__main__':
#         main()
