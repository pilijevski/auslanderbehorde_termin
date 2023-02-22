import time

import chime
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def create_chrome_options():
    # Adding random user agent to avoid bot detection
    # ua = UserAgent()
    # user_agent = ua.random

    options = Options()
    # options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--incognito")
    return options


def create_driver(url):
    options = create_chrome_options()
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get(url)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"""})
    return driver


def chime_n(n):
    i = 0
    while i < n:
        chime.success()
        print("chime")
        time.sleep(1)
        i += 1
