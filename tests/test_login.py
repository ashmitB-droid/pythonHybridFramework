from datetime import datetime
import pytest
from pages.homepage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_with_credentials("testetst1234@gmail.com", "12345")
        assert account_page.verify_account_page_is_displayed()

    def test_login_with_invalid_email(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credentials(self.generate_random_email_with_timestamp(), "12345")
        expected_warning = "No match for E-Mail Address and/or Password"
        assert login_page.verify_login_warning_message().__contains__(expected_warning)

    def test_login_with_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credentials("testetst1234@gmail.com", "adsas1234")
        expected_warning = "No match for E-Mail Address and/or Password"
        assert login_page.verify_login_warning_message().__contains__(expected_warning)

    def test_login_without_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credentials("", "")
        expected_warning = "No match for E-Mail Address and/or Password"
        assert login_page.verify_login_warning_message().__contains__(expected_warning)

    def generate_random_email_with_timestamp(self):
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "testing_"+timestamp+"@gmail.com"
