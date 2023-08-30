from selenium.webdriver.common.by import By
from pages.loginpage import LoginPage
from pages.registerpage import RegisterPage
from pages.searchpage import SearchPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    search_box_field_name = "search"
    search_button_css = "button[class='btn btn-default btn-lg']"
    my_account = "a[title='My Account']"
    login_button = "Login"
    register_button = "Register"

    def enter_product_in_search_box_field(self, product):
        self.driver.find_element(By.NAME, self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product)

    def click_on_search_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.search_button_css).click()
        return SearchPage(self.driver)

    def click_on_my_account_drop_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, self.my_account).click()

    def click_on_login_button_in_dropdown(self):
        self.driver.find_element(By.LINK_TEXT, self.login_button).click()
        return LoginPage(self.driver)

    def click_on_register_button_in_dropdown(self):
        self.driver.find_element(By.LINK_TEXT, self.register_button).click()
        return RegisterPage(self.driver)

    def search_for_product(self, product):
        self.enter_product_in_search_box_field(product)
        return self.click_on_search_button()

    def navigate_to_login_page(self):
        self.click_on_my_account_drop_menu()
        return self.click_on_login_button_in_dropdown()

    def navigate_to_register_page(self):
        self.click_on_my_account_drop_menu()
        return self.click_on_register_button_in_dropdown()


