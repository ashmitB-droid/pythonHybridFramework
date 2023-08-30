from selenium.webdriver.common.by import By

class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    edit_your_account_page_link_text = "Edit your account information"
    account_success_xpath = "//div[@id='content']/h1"

    def verify_account_page_is_displayed(self):
        return self.driver.find_element(By.LINK_TEXT, self.edit_your_account_page_link_text).is_displayed()

    def verify_account_creation_success(self):
        return self.driver.find_element(By.XPATH, self.account_success_xpath).text