import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def print_element_text(element):
    print("Text:", element.text)
    print("Size:", element.size)
    print("Tag name:", element.tag_name)
    print("Location:", element.location)
    print("accessible name:", element.accessible_name)
    print("id:", element.id)
    print("rectangle:", element.rect)


def print_element_properties(element):
    print("Checked state:", element.get_property("checked"))



def print_element_attribute(element):
    print("ID:", element.get_attribute("id"))
    print("Class:", element.get_attribute("Class"))
    print("Style:", element.get_attribute("Style"))
    print("inner Text:", element.get_attribute("inner Text"))
    print("inner HTML:", element.get_attribute("inner HTML"))



def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(" https://academy.testifyltd.com/")
    element = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]')
    testify_link = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]')
    testify = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]')
    print_element_properties(testify)
    print_element_attribute(testify_link)
    print_element_text(element)

    time.sleep(2)




if __name__ == '__main__':
    main()
