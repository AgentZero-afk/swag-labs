import pytest
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from config import URLs


@pytest.fixture()
def checkout_step_two_page(logged_in_browser):
    main_page = MainPage(logged_in_browser, URLs.INVENTORY_URL)
    main_page.add_to_cart()
    main_page.go_to_cart()
    cart_page = CartPage(logged_in_browser, URLs.CART_URL)
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(logged_in_browser, URLs.CHECKOUT_URL)
    checkout_page.fill_form("John", "Doe", "12345")
    checkout_page.click_on_continue_button()
    return CheckoutStepTwoPage(logged_in_browser, URLs.CHECKOUT_STEP_TWO_URL)


@pytest.fixture()
def checkout_step_two_with_expected_data(logged_in_browser):
    main_page = MainPage(logged_in_browser, URLs.INVENTORY_URL)
    expected = {
        "name": main_page.get_product_names()[0],
        "price": main_page.get_product_prices_text()[0],
        "desc": main_page.get_product_desc()[0]
    }
    main_page.add_to_cart()
    main_page.go_to_cart()
    cart_page = CartPage(logged_in_browser, URLs.CART_URL)
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(logged_in_browser, URLs.CHECKOUT_URL)
    checkout_page.fill_form("John", "Doe", "12345")
    checkout_page.click_on_continue_button()
    page = CheckoutStepTwoPage(logged_in_browser, URLs.CHECKOUT_STEP_TWO_URL)
    return page, expected


@pytest.fixture()
def checkout_step_two_multiple_items(logged_in_browser):
    main_page = MainPage(logged_in_browser, URLs.INVENTORY_URL)
    main_page.add_multiple_items_to_cart()
    main_page.go_to_cart()
    cart_page = CartPage(logged_in_browser, URLs.CART_URL)
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(logged_in_browser, URLs.CHECKOUT_URL)
    checkout_page.fill_form("John", "Doe", "12345")
    checkout_page.click_on_continue_button()
    return CheckoutStepTwoPage(logged_in_browser, URLs.CHECKOUT_STEP_TWO_URL)


@pytest.fixture()
def checkout_step_two_multiple_items_with_data(logged_in_browser):
    main_page = MainPage(logged_in_browser, URLs.INVENTORY_URL)
    count = 3
    expected_names = main_page.get_product_names()[:count]
    expected_prices = main_page.get_product_prices_text()[:count]
    main_page.add_multiple_items_to_cart(count)
    main_page.go_to_cart()
    cart_page = CartPage(logged_in_browser, URLs.CART_URL)
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(logged_in_browser, URLs.CHECKOUT_URL)
    checkout_page.fill_form("John", "Doe", "12345")
    checkout_page.click_on_continue_button()
    page = CheckoutStepTwoPage(logged_in_browser, URLs.CHECKOUT_STEP_TWO_URL)
    return page, {"names": expected_names, "prices": expected_prices}


@pytest.mark.checkout
@pytest.mark.smoke
class TestCheckoutStepTwoElements:
    def test_item_title_visible(self, checkout_step_two_page):
        checkout_step_two_page.should_item_title_visible()

    def test_item_description_visible(self, checkout_step_two_page):
        checkout_step_two_page.should_description_visible()

    def test_item_price_visible(self, checkout_step_two_page):
        checkout_step_two_page.should_price_visible()

    def test_item_quantity_visible(self, checkout_step_two_page):
        checkout_step_two_page.should_quantity_visible()

    def test_payment_info_visible(self, checkout_step_two_page):
        checkout_step_two_page.should_payment_info_visible()

    def test_shipping_info_visible(self, checkout_step_two_page):
        checkout_step_two_page.should_shipping_info_visible()

    def test_subtotal_visible(self, checkout_step_two_page):
        checkout_step_two_page.should_subtotal_visible()

    def test_tax_visible(self, checkout_step_two_page):
        checkout_step_two_page.should_tax_visible()

    def test_total_visible(self, checkout_step_two_page):
        checkout_step_two_page.should_total_visible()


@pytest.mark.checkout
@pytest.mark.regression
class TestCheckoutStepTwoFunc:
    def test_finish_button_redirects_to_complete(self, checkout_step_two_page):
        checkout_step_two_page.click_finish()
        checkout_step_two_page.should_redirect_to_checkout_complete()

    def test_cancel_button_redirects_to_inventory(self, checkout_step_two_page):
        checkout_step_two_page.click_cancel()
        checkout_step_two_page.should_redirect_to_inventory()

    def test_cart_items_match_added_data(self, checkout_step_two_with_expected_data):
        page, expected = checkout_step_two_with_expected_data
        page.should_cart_items_eq_added_data(
            expected["name"], expected["price"], expected["desc"]
        )

    def test_multiple_items_count(self, checkout_step_two_multiple_items):
        checkout_step_two_multiple_items.should_cart_items_count_eq(3)

    def test_item_data_persists_after_refresh(self, checkout_step_two_page):
        name_before = checkout_step_two_page.get_item_name()
        price_before = checkout_step_two_page.get_item_price()
        desc_before = checkout_step_two_page.get_item_description()
        checkout_step_two_page.refresh_page()
        checkout_step_two_page.should_cart_items_eq_added_data(
            name_before, price_before, desc_before
        )

    def test_subtotal_plus_tax_equals_total(self, checkout_step_two_page):
        checkout_step_two_page.should_total_eq_subtotal_plus_tax()

    def test_subtotal_equals_sum_of_prices(self, checkout_step_two_multiple_items):
        checkout_step_two_multiple_items.should_subtotal_eq_sum_of_prices()

    def test_quantity_value(self, checkout_step_two_page):
        checkout_step_two_page.should_quantity_eq("1")

    def test_payment_info_value(self, checkout_step_two_page):
        checkout_step_two_page.should_payment_info_not_empty()

    def test_shipping_info_value(self, checkout_step_two_page):
        checkout_step_two_page.should_shipping_info_not_empty()

    def test_multiple_items_data(self, checkout_step_two_multiple_items_with_data):
        page, expected = checkout_step_two_multiple_items_with_data
        page.should_all_items_match(expected["names"], expected["prices"])

    def test_click_item_link_redirects_to_item_page(self, checkout_step_two_page):
        checkout_step_two_page.click_item_link()
        checkout_step_two_page.should_redirect_to_item_page()