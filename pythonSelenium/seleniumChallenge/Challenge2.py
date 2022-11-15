# Challenge 2

# Using the firefox  browser    navigate  to https://www.google.com/
# enter  the text  Python in the search  box, then  send  the  Enter  key.
# Get  the text  from  the Wikipedia brief on the  right side and  print the  value in the console.

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def send_keys_to_google(element, *keys):
    element.send_keys(keys)

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com/")
    send_keys_to_google(driver.find_element(By.XPATH, '//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]'), "Python")
    searchbox = driver.find_element(By.XPATH, "//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[4]/center[1]/input[1]").click()
    print("login:", searchbox)

    text_on_wikipedia = driver.find_element(By.XPATH, "//span[contains(text(),'Python is a high-level, general-purpose programmin')]")
    print("Wikipedia:", text_on_wikipedia.text)
    time.sleep(5)




if __name__ == '__main__':
    main()
