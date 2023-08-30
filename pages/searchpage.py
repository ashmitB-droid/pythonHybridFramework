from pages.base_page import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    searched_item_link_text = "HP LP3065"
    no_product_found_xpath = "//input[@id='button-search']/following-sibling::p"

    def verify_searched_item_displayed(self):
        return self.element_display("searched_item_link_text", self.searched_item_link_text)

    def get_no_product_message(self):
        return self.get_text_message("no_product_found_xpath", self.no_product_found_xpath)

