import pytest
from selenium import webdriver
import configparser
@pytest.fixture(autouse=True)
def selenium_driver(request):
    # Initialize the WebDriver
    driver = webdriver.Firefox()

    # Set an implicit wait to handle elements that may not be immediately present
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Provide the WebDriver instance to the test function
    request.cls.driver=driver
    yield

    # Teardown: Close the WebDriver instance
    driver.quit()


def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Settings']['url']

