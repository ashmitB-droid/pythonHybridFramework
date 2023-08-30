import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities import ConfigReader


# Needs fixing for generating screenshot on failure
# @pytest.fixture()
# # def screenshot_on_failure(request):
# #     yield
# #     item = request.node
# #     if item.rep_call.failed:
# #         allure.attach(driver.get_screenshot_as_png(), failed= "failed_test_screenshot",
# #                       attachment_type=AttachmentType.PNG)
# #
# #
# # @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# # def pytest_runtest_makereport(item, call):
# #     outcome = yield
# #     rep = outcome.get_result()
# #     setattr(item, "rep_" + rep.when, rep)
# #     return rep

@pytest.fixture()
def setup_and_teardown(request):
    browser = ConfigReader.read_configuration("basic info", "browser")
    global driver
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
    url = ConfigReader.read_configuration("basic info", "url")
    driver.get("https://tutorialsninja.com/demo/")
    # this is what enable all classes to get driver to all classes
    request.cls.driver = driver
    yield
    # time.sleep(100)
    driver.quit()