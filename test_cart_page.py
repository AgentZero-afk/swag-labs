import pytest
from pages import MainPage
from pages.cart_page import CartPage
from config import URLs
from conftest import _logout_and_login


@pytest.fixture()
def cart_page(logged_in_browser):
    main_page = MainPage(logged_in_browser, URLs.INVENTORY_URL)
    main_page.add_to_cart()
    main_page.go_to_cart()
    cart_page = CartPage(logged_in_browser, URLs.CART_URL)
    return cart_page

@pytest.fixture()
def cart_page_with_items(logged_in_browser):
    main_page = MainPage(logged_in_browser, URLs.INVENTORY_URL)
    main_page.add_multiple_items_to_cart()
    main_page.go_to_cart()
    cart_page_with_items = CartPage(logged_in_browser, URLs.CART_URL)
    return cart_page_with_items

@pytest.fixture()
def cart_with_expected_data(logged_in_browser):
    main_page = MainPage(logged_in_browser, URLs.INVENTORY_URL)
    expected = {
        "name": main_page.get_product_names()[0],
        "price": main_page.get_product_prices_text()[0],
        "desc": main_page.get_product_desc()[0]
    }
    main_page.add_to_cart()
    main_page.go_to_cart()
    cart_page_with_expected_data = CartPage(logged_in_browser, URLs.CART_URL)
    return cart_page_with_expected_data,expected

@pytest.fixture()
def empty_cart_page(logged_in_browser):
    main_page = MainPage(logged_in_browser, URLs.INVENTORY_URL)
    main_page.go_to_cart()
    return CartPage(logged_in_browser, URLs.CART_URL)

@pytest.fixture()
def cart_page_relog(logged_in_browser):
    main_page = MainPage(logged_in_browser, URLs.INVENTORY_URL)
    main_page.add_to_cart()
    _logout_and_login(logged_in_browser)
    MainPage(logged_in_browser, URLs.INVENTORY_URL).go_to_cart()
    return CartPage(logged_in_browser, URLs.CART_URL)

@pytest.mark.cart
@pytest.mark.regression
class TestFuncButtons:
    def test_remove_from_cart(self, cart_page):
        cart_page.remove_from_cart()
        cart_page.should_item_removed_from_cart()

    def test_remove_items_from_cart(self, cart_page_with_items):
        cart_page_with_items.remove_items_from_cart()
        cart_page_with_items.should_cart_items_count_eq(0)

    def test_items_count_in_cart(self, cart_page_with_items):
        cart_page_with_items.should_cart_items_count_eq(3)

    def test_back_to_item_list(self, cart_page):
        cart_page.back_to_item_list()
        cart_page.should_be_back_to_item_list()

    def test_checkout_button(self, cart_page):
        cart_page.go_to_checkout()
        cart_page.should_redirect_to_checkout()

    def test_go_to_item_page(self, cart_page):
        cart_page.click_on_item()
        cart_page.should_redirect_to_item_page("4")

    def test_remove_one_item_from_multiple(self,cart_page_with_items):
        count_before = cart_page_with_items.get_cart_items_count()
        cart_page_with_items.remove_from_cart()
        cart_page_with_items.should_cart_items_count_eq(count_before - 1)

    def test_cart_persists_after_navigation(self,cart_page_relog):
        cart_page_relog.should_cart_items_count_eq(1)

    def test_cart_items_match_added_items(self, cart_with_expected_data):
        cart_page_with_expected_data,expected = cart_with_expected_data
        cart_page_with_expected_data.should_cart_items_eq_add_items_data(
            expected["name"], expected["price"], expected["desc"]
        )

    def test_continue_shopping_from_empty_cart(self,empty_cart_page):
        empty_cart_page.back_to_item_list()
        empty_cart_page.should_be_back_to_item_list()

    def test_correct_item_remove(self,cart_page_with_items):
        names_before = cart_page_with_items.get_all_item_names()
        removed_name = names_before[0]
        cart_page_with_items.remove_from_cart()
        names_after = cart_page_with_items.get_all_item_names()
        cart_page_with_items.should_remove_but_still_in_cart(names_before, removed_name, names_after)

@pytest.mark.cart
@pytest.mark.smoke
class TestElementCartPage:
    def test_description_visibility(self, cart_page):
        cart_page.should_description_visible()

    def test_item_price_visibility(self, cart_page):
        cart_page.should_price_visible()

    def test_item_title_visibility(self, cart_page):
        cart_page.should_item_title_visible()

    def test_empty_cart_has_no_items(self,empty_cart_page):
        empty_cart_page.should_cart_items_count_eq(0)

    def test_cart_quantity_visible(self,cart_page):
        cart_page.should_quantity_visible()

    def test_item_save_after_refresh(self,cart_page):
        count_before = cart_page.get_cart_items_count()
        cart_page.refresh_page()
        cart_page.should_cart_items_count_eq(count_before)







