import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Challenge 5
# Using any browser, navigate to any Youtube video of your choice, allow your script to wait for the comments to load
# then get the first two comments, and print them in the terminal.
def scroll_by_offset(action, delta_y):
    action.scroll_by_amount(0, delta_y).perform()

def sweet_test(driver):
    driver.get("https://www.youtube.com/watch?v=VGecJY7u6So")
    action = ActionChains(driver)
    driver.maximize_window()
    # time.sleep(60)
    scroll_by_offset(action, 450)
    web_driver_wait = WebDriverWait(driver, 60)
    web_driver_wait.until(EC.visibility_of_element_located((By.TAG_NAME, "ytd-comment-renderer")))

    comments = driver.find_elements(By.TAG_NAME, 'ytd-comment-renderer') 
    for comment in comments:
        comment_content = comment.find_element(By.ID, 'content-text')
        print(comment_content.text)

def main():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    gecko_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    edge_driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    sweet_test(chrome_driver)
    sweet_test(gecko_driver)
    sweet_test(edge_driver)


    time.sleep(15)


if __name__ == '__main__':
    main()
