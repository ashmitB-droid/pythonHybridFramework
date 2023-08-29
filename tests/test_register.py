import time
from datetime import datetime

import pytest
from pages.accountpage import AccountPage
from pages.homepage import HomePage
from pages.registerpage import RegisterPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def generate_random_email_with_timestamp(self):
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "testing_"+timestamp+"@gmail.com"

    def test_register_with_all_the_mandatory_fields(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        register_page = RegisterPage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.click_on_register_button_in_dropdown()
        register_page.enter_firstname("Arun")
        register_page.enter_lastname("ji")
        register_page.enter_email(self.generate_random_email_with_timestamp())
        register_page.enter_telephone('1234567890')
        register_page.enter_password('12345')
        register_page.confirm_password('12345')
        register_page.click_on_agree_policy_button()
        register_page.click_on_continue_button()
        account_msg = 'Your Account Has Been Created!'
        assert account_page.verify_account_creation_success().__contains__(account_msg)

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        register_page = RegisterPage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.click_on_register_button_in_dropdown()
        register_page.enter_firstname("Arun")
        register_page.enter_lastname("ji")
        register_page.enter_email(self.generate_random_email_with_timestamp())
        register_page.enter_telephone('1234567890')
        register_page.enter_password('12345')
        register_page.confirm_password('12345')
        register_page.click_newsletter_radio_button()
        register_page.click_on_agree_policy_button()
        register_page.click_on_continue_button()
        account_msg = 'Your Account Has Been Created!'
        assert account_page.verify_account_creation_success().__contains__(account_msg)

    def test_register_with_existing_email(self):
        home_page = HomePage(self.driver)
        register_page = RegisterPage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.click_on_register_button_in_dropdown()
        register_page.enter_firstname("Arun")
        register_page.enter_lastname("ji")
        register_page.enter_email("testetst1234@gmail.com")
        register_page.enter_telephone('1234567890')
        register_page.enter_password('12345')
        register_page.confirm_password('12345')
        register_page.click_on_agree_policy_button()
        register_page.click_on_continue_button()
        account_msg = 'E-Mail Address is already registered!'
        assert register_page.get_registration_warning_message().__contains__(account_msg)

    def test_register_without_entering_any_field(self):
        home_page = HomePage(self.driver)
        register_page = RegisterPage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.click_on_register_button_in_dropdown()
        register_page.enter_firstname("")
        register_page.enter_lastname("")
        register_page.enter_email("")
        register_page.enter_telephone('')
        register_page.enter_password('')
        register_page.confirm_password('')
        register_page.click_on_agree_policy_button()
        register_page.click_on_continue_button()
        privacy_msg = 'First Name must be between'
        assert register_page.get_empty_first_name_message().__contains__(privacy_msg)


