from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    searched_item_link = "HP LP3065"
    no_product_found_for_search = "//input[@id='button-search']/following-sibling::p"

    def verify_searched_item_displayed(self):
        return self.driver.find_element(By.LINK_TEXT, self.searched_item_link).is_displayed()

    def get_no_product_message(self):
        return self.driver.find_element(By.XPATH, self.no_product_found_for_search).text

