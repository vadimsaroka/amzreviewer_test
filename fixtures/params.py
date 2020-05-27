from datetime import date
from random import randint
import os
from selenium.webdriver import Chrome

DOMAIN = "https://amzreviewer.now.sh"

USER_NAME = "Testuser"
DEFAULT_PASSWORD = "12345678"
DEFAULT_EMAIL = "test@gmail.com"

cwd = os.path.abspath(os.getcwd())

CHROME_EXECUTABLE_PATH = Chrome()
FIREFOX_EXECUTABLE_PATH = os.path.join(cwd, "driver/geckodriver")

BROWSER_TYPE = "Chrome"

EXPLICIT_TIMEOUT = 10

# PRODUCT_NAME = f"VS Product # {str(randint(1, 100))}"
PRODUCT_NAME = "vs product name"
PRICE = '25.99'
ORDER_NUMBER = "111-222-333-444-555"
GROUP_NAME = 'testgroupname'
DATE = date.today().strftime("%m/%d/%y")




