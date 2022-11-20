#  Navigate any browser to https://weather.com/ get the
#  current temperature and print it out in the terminal.
#  Then print out the temperature for Morning, Afternoon, Evening,and Overnight.


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
    driver.get("https://weather.com/")
 
    # current temperature
    current_temperature = driver.find_element(By.XPATH, '//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[2]/div[1]/div[1]/span')
    print("current temperature:", current_temperature.text)


    # Morning Temperature
    morning_temperature = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[1]/a/div[1]/span')
    print("Morning Temperature:", morning_temperature.text)

    # Afternoon Temperature
    afternoon_temperature = driver.find_element(By.XPATH, "//body/div[@id='appWrapper']/main[@id='MainContent']/div[2]/main[1]/div[3]/section[1]/div[1]/ul[1]/li[2]/a[1]/div[1]/span[1]")
    print("Afternoon Temperature:", afternoon_temperature.text)

    # Evening Temperature
    evening_temperature = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[3]/a/div[1]/span')
    print("Evening Temperature:", evening_temperature.text)

    # Night Temperature
    night_temperature = driver.find_element(By.XPATH, "//body/div[@id='appWrapper']/main[@id='MainContent']/div[2]/main[1]/div[3]/section[1]/div[1]/ul[1]/li[4]/a[1]/div[1]/span[1]")
    print("Night Temperature:", night_temperature.text)
    time.sleep(6)


if __name__ == '__main__':
    main()
