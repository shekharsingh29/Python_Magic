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
    driver.get("https://appbrewery.github.io/instant_pot/")
    title = driver.title
    print(f"The page title is {title}")
    driver.implicitly_wait(0.5)
    dollar_symbol = driver.find_element(by=By.CLASS_NAME, value="a-price-symbol")
    dollar_whole = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")
    dollar_frac = driver.find_element(by=By.CLASS_NAME, value="a-price-fraction")
    # message = driver.find_element(by=By.ID, value="message")

    message = dollar_symbol.text + dollar_whole.text +"."+ dollar_frac.text

    print(f"The price of instant pot is {message}")
    time.sleep(5)
    driver.close()


test_selenium()
