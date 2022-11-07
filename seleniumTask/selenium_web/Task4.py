import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://web.facebook.com/?_rdc=1&_rdr")

    send_keys_to_element(driver.find_element(By.NAME, "email"), "Henryokolie615@gmail.com")
    send_keys_to_element(driver.find_element(By.NAME, "pass"), "Adaobi93/")

    login = driver.find_element(By.NAME, "login").click()
    print("login:", login)
    time.sleep(20)


if __name__ == '__main__':
    main()
