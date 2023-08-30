from selenium.webdriver.common.by import By
from pages.accountpage import AccountPage
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    email_field_id = "input-email"
    password_field_id = "input-password"
    login_button_css = "input[value='Login']"
    login_warning_message_css = ".alert.alert-danger.alert-dismissible"

    def enter_email_in_input_field(self, email_text):
        self.type_in_field("email_field_id", self.email_field_id, email_text)

    def enter_password_in_input_field(self, password_text):
        self.type_in_field("password_field_id", self.password_field_id, password_text)

    def click_login_button(self):
        self.click_on_button("login_button_css", self.login_button_css)
        return AccountPage(self.driver)

    def verify_login_warning_message(self):
        return self.get_text_message("login_warning_message_css", self.login_warning_message_css)

    def login_with_credentials(self, email_text, password_text):
        self.enter_email_in_input_field(email_text)
        self.enter_password_in_input_field(password_text)
        return self.click_login_button()