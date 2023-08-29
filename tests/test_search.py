import pytest
from selenium.webdriver.common.by import By

from pages.homepage import HomePage
from pages.searchpage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        home_page.enter_product_in_search_box_field("HP")
        home_page.click_on_search_button()
        assert search_page.verify_searched_item_displayed()

    def test_search_for_an_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        home_page.enter_product_in_search_box_field("Honda")
        home_page.click_on_search_button()
        expected_text = 'There is no product that matches the search criteria.'
        assert search_page.get_no_product_message().__eq__(expected_text)

    def test_search_without_any_product(self):
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        home_page.enter_product_in_search_box_field("")
        home_page.click_on_search_button()
        expected_text = 'There is no product that matches the search criteria.'
        assert search_page.get_no_product_message().__eq__(expected_text)
