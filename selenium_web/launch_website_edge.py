import time

from selenium import webdriver

def main():
    driver = webdriver.Edge(executable_path=r"C:\Users\Henmis\Desktop\TESTIFY SCHOOL\webdriver/msedgedriver.exe")
    driver.get("https://www.google.com/")
    time.sleep(20)
    driver.close()



main()