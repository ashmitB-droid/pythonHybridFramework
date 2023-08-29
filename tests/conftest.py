import time

import pytest
from selenium import webdriver

from utilities import config_reader


@pytest.fixture()
def setup_and_teardown(request):
    browser = config_reader.read_configuration("basic info", "browser")
    driver = None
    if browser.__eq__('chrome'):
        driver = webdriver.Chrome()
    elif browser.__eq__('firefox'):
        driver = webdriver.Firefox()
    elif browser.__eq__('edge'):
        driver = webdriver.edge()
    else:
        print('Please enter a valid driver in the config file')
    driver.maximize_window()
    url = config_reader.read_configuration("basic info", "url")
    driver.get("https://tutorialsninja.com/demo/")
    # this is what enable all classes to get driver to all classes
    request.cls.driver = driver
    yield
    # time.sleep(300)
    driver.quit()