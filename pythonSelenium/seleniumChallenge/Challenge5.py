# Challenge 5
# Using any browser navigate to any Youtube video of yourchoice,
# allow your script to wait for the comments to load thenget the
# first two comments, and print them in the terminal.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_check_youtube(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.youtube.com/watch?v=-E74uXVVDcg")
    first_comment = driver.find_elements(By.LINK_TEXT, "I’m 13 years old, it’s so hard to be a Christian teenager and many teenagers don’t believe in Jesus but i want them to believe in Jesus I’ll pray for them everyday and I’ll keep my faith foreve")
    print("first Comment:", first_comment)

    second_comment = driver.find_elements(By.XPATH, '/html[1]/body[1]/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-watch-flexy[1]/div[5]/div[1]/div[1]/div[2]/ytd-comments[1]/ytd-item-section-renderer[1]/div[3]/ytd-comment-thread-renderer[4]/ytd-comment-renderer[1]/div[3]/div[2]/div[2]/ytd-expander[1]/div[1]/yt-formatted-string[1]')
    print("Second Comment:", list(second_comment))
    time.sleep(10)


if __name__ == '__main__':
    main()
