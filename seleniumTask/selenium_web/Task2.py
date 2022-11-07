import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def locate_by_name(driver):

    text_element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/div/button/span[1]')
    print("Text Element", text_element)
    subscribe_element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[8]/div/div/div[3]/form/button').click()
    print("Subscribe Element", subscribe_element)




def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(" https://academy.testifyltd.com/")
    locate_by_name(driver)



if __name__ == '__main__':
    main()
