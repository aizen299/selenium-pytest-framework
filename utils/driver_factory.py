import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

SLOW_MODE_DELAY = float(os.getenv("SLOW_MODE", "0.1"))

class SlowChrome(webdriver.Chrome):
    def slow(self):
        time.sleep(SLOW_MODE_DELAY)

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    service = Service(ChromeDriverManager().install())
    driver = SlowChrome(service=service, options=options)
    return driver