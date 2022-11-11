# Challenge 4

# Navigate to https://www.bbc.com/ and print out the top 10 latest news from the home page.

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def send_keys_to_check_weather(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.bbc.com/")

    news = driver.find_element(By.LINK_TEXT, "News").click()
    print("News:", news)

    # 1st news
    _1st_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]")
    print("1st News:", _1st_news.text)

    # # 2nd news
    second_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/a[1]")
    print("2nd News:", second_news.text)

    # 3rd news
    _3rd_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[8]/div[1]/div[2]/div[1]/a[1]")
    print("3rd News:", _3rd_news.text)

    # # 4th News
    _4th_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[9]/div[1]/div[2]/div[1]/a[1]")
    print("4th News:", _4th_news.text)

    # 5th News
    _5th_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[11]/div[1]/div[2]/div[1]/a[1]")
    print("5th News:", _5th_news.text)

    # 6th News
    _6th_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[13]/div[1]/div[1]/div[2]/div[1]/a[1]")
    print("6th News:", _6th_news.text)

    # 7th News
    _7th_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[15]/div[5]/div[1]/div[2]/div[1]/a[1]")
    print("7th News:", _7th_news.text)

    # 8th News
    _8th_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[15]/div[2]/div[1]/div[2]/div[1]/a[1]")
    print("8th News:", _8th_news.text)

    # 9th News
    _9th_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[15]/div[3]/div[1]/div[2]/div[1]/a[1]")
    print("9th News:", _9th_news.text)

    # 10th News
    _10th_news = driver.find_element(By.XPATH, "//body/div[@id='orb-modules']/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[15]/div[4]/div[1]/div[2]/div[1]/a[1]")
    print("10th News:", _10th_news.text)


if __name__ == '__main__':
    main()
