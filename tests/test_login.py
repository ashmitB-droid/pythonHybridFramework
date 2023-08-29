from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from pages.accountpage import AccountPage
from pages.homepage import HomePage
from pages.loginpage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        account_page = AccountPage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.click_on_login_button_in_dropdown()
        login_page.enter_email_in_input_field('testetst1234@gmail.com')
        login_page.enter_password_in_input_field('12345')
        login_page.click_login_button()
        assert account_page.verify_account_page_is_displayed()

    def test_login_with_invalid_email(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.click_on_login_button_in_dropdown()
        login_page.enter_email_in_input_field(self.generate_random_email_with_timestamp())
        login_page.enter_password_in_input_field('12345')
        login_page.click_login_button()
        expected_warning = "No match for E-Mail Address and/or Password"
        assert login_page.verify_login_warning_message().__contains__(expected_warning)

    def test_login_with_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.click_on_login_button_in_dropdown()
        login_page.enter_email_in_input_field("testetst1234@gmail.com")
        login_page.enter_password_in_input_field('adsas1234')
        login_page.click_login_button()
        expected_warning = "No match for E-Mail Address and/or Password"
        assert login_page.verify_login_warning_message().__contains__(expected_warning)

    def test_login_without_credentials(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.click_on_login_button_in_dropdown()
        login_page.enter_email_in_input_field("")
        login_page.enter_password_in_input_field("")
        login_page.click_login_button()
        expected_warning = "No match for E-Mail Address and/or Password"
        assert login_page.verify_login_warning_message().__contains__(expected_warning)

    def generate_random_email_with_timestamp(self):
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "testing_"+timestamp+"@gmail.com"
