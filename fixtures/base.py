import unittest
from time import sleep
from selenium.webdriver.support import expected_conditions as ec
from .params import CHROME_EXECUTABLE_PATH, EXPLICIT_TIMEOUT, BROWSER_TYPE, FIREFOX_EXECUTABLE_PATH
from selenium.webdriver.support.ui import WebDriverWait


def get_browser():
    if BROWSER_TYPE.lower().find("chrome") >= 0:
        browser = CHROME_EXECUTABLE_PATH
    elif BROWSER_TYPE.lower().find("firefox") >= 0:
        browser = FIREFOX_EXECUTABLE_PATH
    else:
        raise Exception(f"I'm sorry {BROWSER_TYPE} browser is not supported")
    return browser


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = get_browser()
        self.wait = WebDriverWait(self.driver, timeout=EXPLICIT_TIMEOUT, poll_frequency=1)
        self.page_url = None

    # def tearDown(self):
    #     self.driver.quit()

    def go_to_page(self):
        sleep(2)
        self.driver.get(self.page_url)
        self.wait.until(ec.url_to_be(self.page_url))


if __name__ == '__main__':
    unittest.main()
