import pytest
from pages.main_page import MainPage
from config import URLs


@pytest.fixture
def main_page(logged_in_browser):
    return MainPage(logged_in_browser, URLs.INVENTORY_URL)


@pytest.mark.regression
class TestSorting:
    def test_sort_by_price_high_to_low(self, main_page):
        main_page.sort_by_price_high_to_low()
        main_page.should_be_sorted_by_price_high_to_low()

    def test_sort_by_price_low_to_high(self, main_page):
        main_page.sort_by_price_low_to_high()
        main_page.should_be_sorted_by_price_low_to_high()

    def test_sort_by_name_z_to_a(self, main_page):
        main_page.sort_by_name_z_to_a()
        main_page.should_be_sorted_by_name_z_to_a()

    def test_sort_by_name_a_to_z(self, main_page):
        main_page.sort_by_name_a_to_z()
        main_page.should_be_sorted_by_name_a_to_z()


@pytest.mark.cart
class TestCart:
    def test_add_to_cart_shows_badge(self, main_page):
        main_page.add_to_cart()
        main_page.should_show_badge_after_add_to_cart()

    def test_remove_from_cart_hides_badge(self, main_page):
        main_page.add_to_cart()
        main_page.remove_from_cart()
        main_page.should_hide_badge_after_remove_from_cart()

    def test_cart_count_updates_correctly(self, main_page):
        main_page.add_multiple_items_to_cart()
        main_page.should_have_cart_count("3")
        main_page.remove_from_cart()
        main_page.should_have_cart_count("2")


@pytest.mark.navigation
class TestProductNavigation:
    def test_redirect_to_product_page(self, main_page):
        main_page.click_product_link()
        main_page.should_redirect_to_product_page("4")
