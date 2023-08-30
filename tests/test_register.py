from datetime import datetime
import pytest
from pages.homepage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def generate_random_email_with_timestamp(self):
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "testing_"+timestamp+"@gmail.com"

    def test_register_with_all_the_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_page = register_page.register_with_fields("Arun", "ji", self.generate_random_email_with_timestamp(),
                                                          '1234567890', '12345', '12345')
        account_msg = 'Your Account Has Been Created!'
        assert account_page.verify_account_creation_success().__contains__(account_msg)

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page = home_page.click_on_register_button_in_dropdown()
        account_page = register_page.register_with_fields("Arun", "ji", self.generate_random_email_with_timestamp(),
                                                          '1234567890', '12345', '12345', news_letter=True)
        account_msg = 'Your Account Has Been Created!'
        assert account_page.verify_account_creation_success().__contains__(account_msg)

    def test_register_with_existing_email(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page = home_page.click_on_register_button_in_dropdown()
        register_page.register_with_fields("Arun", "ji", "testetst1234@gmail.com",
                                           '1234567890', '12345', '12345')
        account_msg = 'E-Mail Address is already registered!'
        assert register_page.get_registration_warning_message().__contains__(account_msg)

    def test_register_without_entering_any_field(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        register_page = home_page.click_on_register_button_in_dropdown()
        register_page.register_with_fields("", "", "", "", "", "", False)
        privacy_msg = 'First Name must be between'
        assert register_page.get_empty_first_name_message().__contains__(privacy_msg)


