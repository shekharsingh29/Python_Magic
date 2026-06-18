from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome()
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Firefox()

def test_selenium():
    driver.get("https://www.python.org/")
    title = driver.title
    print(f"The page title is {title}")
    driver.implicitly_wait(0.5)
    upcoming_elements = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget .menu li")

    # message = driver.find_element(by=By.ID, value="message")
    events = []
    for elm in upcoming_elements:
        print(f"The event is {elm.text}")
        events.append({'time':elm.find_element(By.TAG_NAME,'time').text,'name':elm.find_element(By.TAG_NAME,'a').text})

    print(events)
    time.sleep(5)
    driver.close()


test_selenium()
