from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def locate_by_id(driver):
    email_element = driver.find_element(By.ID, "email")
    print("Element", email_element)
    password_element = driver.find_element(By.ID, "pass")
    print("Element", password_element)


def locate_by_name(driver):
    firstname_element = driver.find_element(By.NAME, "firstname")
    print("FristnameElement", firstname_element)
    lastname_element = driver.find_element(By.NAME, "lastname")
    print("Lastname Element", lastname_element)



def locate_by_class_name(driver):
    rr_first_element = driver.find_element(By.CLASS_NAME, "react-reveal")
    print("React Reveal First Element", rr_first_element)
    rr_elements = driver.find_elements(By.CLASS_NAME, "react-reveal")
    for rr_element in rr_elements:
        print("React Reveal Elements", rr_element)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    # locate_by_id(driver)
    # locate_by_name(driver)
    locate_by_class_name(driver)




if __name__ == '__main__':
    main()
