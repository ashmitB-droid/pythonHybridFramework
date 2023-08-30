from selenium.webdriver.common.by import By
from pages.accountpage import AccountPage


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    firstname_field = "input-firstname"
    lastname_field = "input-lastname"
    email_field = "input-email"
    telephone_field = "input-telephone"
    password_field = "input-password"
    confirm_password_field = "input-confirm"
    agree_policy = "agree"
    continue_button = "input[value='Continue']"
    get_newsletter_radio = "//input[@name='newsletter'][@value='1']"
    registration_warning_message = "//div[@id='account-register']/div[1]"
    empty_first_name = "//input[@name='firstname']/following-sibling::div"

    def enter_firstname(self, firstname_text):
        self.driver.find_element(By.ID, self.firstname_field).click()
        self.driver.find_element(By.ID, self.firstname_field).clear()
        self.driver.find_element(By.ID, self.firstname_field).send_keys(firstname_text)

    def enter_lastname(self, lastname_text):
        self.driver.find_element(By.ID, self.lastname_field).click()
        self.driver.find_element(By.ID, self.lastname_field).clear()
        self.driver.find_element(By.ID, self.lastname_field).send_keys(lastname_text)

    def enter_email(self, email_text):
        self.driver.find_element(By.ID, self.email_field).click()
        self.driver.find_element(By.ID, self.email_field).clear()
        self.driver.find_element(By.ID, self.email_field).send_keys(email_text)

    def enter_telephone(self, telephone_text):
        self.driver.find_element(By.ID, self.telephone_field).click()
        self.driver.find_element(By.ID, self.telephone_field).clear()
        self.driver.find_element(By.ID, self.telephone_field).send_keys(telephone_text)

    def enter_password(self, password_text):
        self.driver.find_element(By.ID, self.password_field).click()
        self.driver.find_element(By.ID, self.password_field).clear()
        self.driver.find_element(By.ID, self.password_field).send_keys(password_text)

    def confirm_password(self, confirm_password):
        self.driver.find_element(By.ID, self.confirm_password_field).click()
        self.driver.find_element(By.ID, self.confirm_password_field).clear()
        self.driver.find_element(By.ID, self.confirm_password_field).send_keys(confirm_password)

    def click_on_agree_policy_button(self):
        self.driver.find_element(By.NAME, self.agree_policy).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.continue_button).click()
        return AccountPage(self.driver)

    def click_newsletter_radio_button(self):
        self.driver.find_element(By.XPATH, self.get_newsletter_radio).click()

    def get_registration_warning_message(self):
        return self.driver.find_element(By.XPATH, self.registration_warning_message).text

    def get_empty_first_name_message(self):
        return self.driver.find_element(By.XPATH, self.empty_first_name).text

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
