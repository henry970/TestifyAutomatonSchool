# Challenge 2

# Using the firefox  browser    navigate  to https://www.google.com/
# enter  the text  Python in the search  box, then  send  the  Enter  key.
# Get  the text  from  the Wikipedia brief on the  right side and  print the  value in the console.

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def send_keys_to_google(element, *keys):
    element.send_keys(keys)

def main():
   driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.google.com/")
    send_keys_to_google(driver.find_element(By.XPATH, '//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]'), "Python")
    searchbox = driver.find_element(By.XPATH, "//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[4]/center[1]/input[1]").click()
    print("login:", searchbox)

    text_on_wikipedia = driver.find_element(By.XPATH, "//span[contains(text(),'Python is a high-level, general-purpose programmin')]")
    print("Wikipedia:", text_on_wikipedia.text)
    time.sleep(5)




if __name__ == '__main__':
    main()
