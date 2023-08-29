from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver


    email_field = "input-email"
    password_field = "input-password"
    login_button = "input[value='Login']"
    login_warning_message = ".alert.alert-danger.alert-dismissible"

    def enter_email_in_input_field(self, email_text):
        self.driver.find_element(By.ID, self.email_field).click()
        self.driver.find_element(By.ID, self.email_field).clear()
        self.driver.find_element(By.ID, self.email_field).send_keys(email_text)

    def enter_password_in_input_field(self, password_text):
        self.driver.find_element(By.ID, self.password_field).click()
        self.driver.find_element(By.ID, self.password_field).clear()
        self.driver.find_element(By.ID, self.password_field).send_keys(password_text)

    def click_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button).click()

    def verify_login_warning_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.login_warning_message).text