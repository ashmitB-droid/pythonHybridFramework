import pytest
from pages.homepage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_product("HP")
        assert search_page.verify_searched_item_displayed()

    def test_search_for_an_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_product("Honda")
        expected_text = 'There is no product that matches the search criteria.'
        assert search_page.get_no_product_message().__eq__(expected_text)

    def test_search_without_any_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_product("")
        expected_text = 'There is no product that matches the search criteria.'
        assert search_page.get_no_product_message().__eq__(expected_text)
