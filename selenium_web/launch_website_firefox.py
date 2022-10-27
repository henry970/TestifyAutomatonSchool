import time

from selenium import webdriver


def main():
    driver = webdriver.Firefox(executable_path=r"C:\Users\Henmis\Desktop\TESTIFY SCHOOL\webdriver/geckodriver.exe")
    driver.get("https://www.google.com/")
    time.sleep(20)
    driver.close()




main()

