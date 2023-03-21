import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# options = Options()
# options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    driver.maximize_window()

    driver.get("https://www.google.com")

    driver.find_element("name","q").send_keys("selenium")
    driver.find_element("name","q").send_keys(Keys.ENTER)

    time.sleep(3)
    print("The first web test completed successfully!")
finally:
    driver.close()

