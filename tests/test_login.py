import pytest
from pages.homepage import HomePage
from tests.base_test import BaseTest
from utilities import ExcelUtil


class TestLogin(BaseTest):

    @pytest.mark.parametrize("email_address, password", ExcelUtil.get_data_from_excel(
        "testDataFile/testdata.xlsx", "loginData"))
    def test_login_with_valid_credentials(self, email_address, password):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_with_credentials(email_address, password)
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

