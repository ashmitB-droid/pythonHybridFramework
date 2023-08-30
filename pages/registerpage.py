from selenium.webdriver.common.by import By
from pages.accountpage import AccountPage
from pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    firstname_field_id = "input-firstname"
    lastname_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    agree_policy_name = "agree"
    continue_button_css = "input[value='Continue']"
    get_newsletter_radio_xpath = "//input[@name='newsletter'][@value='1']"
    registration_warning_message_xpath = "//div[@id='account-register']/div[1]"
    empty_first_name_xpath = "//input[@name='firstname']/following-sibling::div"

    def enter_firstname(self, firstname_text):
        self.type_in_field("firstname_field_id", self.firstname_field_id, firstname_text)

    def enter_lastname(self, lastname_text):
        self.type_in_field("lastname_field_id", self.lastname_field_id, lastname_text)

    def enter_email(self, email_text):
        self.type_in_field("email_field_id", self.email_field_id, email_text)

    def enter_telephone(self, telephone_text):
        self.type_in_field("telephone_field_id", self.telephone_field_id, telephone_text)

    def enter_password(self, password_text):
        self.type_in_field("password_field_id", self.password_field_id, password_text)

    def confirm_password(self, confirm_password):
        self.type_in_field("confirm_password_field_id", self.confirm_password_field_id, confirm_password)

    def click_on_agree_policy_button(self):
        self.click_on_button("agree_policy_name", self.agree_policy_name)

    def click_on_continue_button(self):
        self.click_on_button("continue_button_css", self.continue_button_css)
        return AccountPage(self.driver)

    def click_newsletter_radio_button(self):
        self.click_on_button("get_newsletter_radio_xpath", self.get_newsletter_radio_xpath)

    def get_registration_warning_message(self):
        return self.get_text_message("registration_warning_message_xpath", self.registration_warning_message_xpath)

    def get_empty_first_name_message(self):
        return self.get_text_message("empty_first_name_xpath", self.empty_first_name_xpath)

    def register_with_fields(self, firstname_text, lastname_text, email_text, telephone_text, password_text,
                             confirm_password, agree_policy=True, news_letter=False):
        self.enter_firstname(firstname_text)
        self.enter_lastname(lastname_text)
        self.enter_email(email_text)
        self.enter_telephone(telephone_text)
        self.enter_password(password_text)
        self.confirm_password(confirm_password)
        if news_letter:
            self.click_newsletter_radio_button()
        if agree_policy:
            self.click_on_agree_policy_button()
        return self.click_on_continue_button()
