from selenium.webdriver.common.by import By


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

    def click_on_my_account_drop_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, self.my_account).click()

    def click_on_login_button_in_dropdown(self):
        self.driver.find_element(By.LINK_TEXT, self.login_button ).click()

    def click_on_register_button_in_dropdown(self):
        self.driver.find_element(By.LINK_TEXT, self.register_button).click()

