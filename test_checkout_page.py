import pytest
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config import URLs


@pytest.fixture
def checkout_page(logged_in_browser):
    main_page = MainPage(logged_in_browser, URLs.INVENTORY_URL)
    main_page.add_to_cart()
    main_page.go_to_cart()
    cart_page = CartPage(logged_in_browser, URLs.CART_URL)
    cart_page.go_to_checkout()
    return CheckoutPage(logged_in_browser, URLs.CHECKOUT_URL)

@pytest.mark.checkout
@pytest.mark.regression
class TestCheckoutFunc:

    @pytest.mark.parametrize("first_name, last_name, postal_code, expected_error",[
        ("","Doe","12345","Error: First Name is required"),
        ("John","","12345","Error: Last Name is required"),
        ("John","Doe","","Error: Postal Code is required"),
        ("","","","Error: First Name is required")
    ])
    def test_form_validation_errors(self,checkout_page, first_name, last_name, postal_code, expected_error):
        checkout_page.fill_form(first_name, last_name, postal_code)
        checkout_page.click_on_continue_button()
        checkout_page.should_show_error(expected_error)

    def test_valid_form_submit(self, checkout_page):
        checkout_page.fill_form("John","Doe","12345")
        checkout_page.click_on_continue_button()
        checkout_page.should_go_to_checkout_page_step_two()

    def test_cancel_button_go_to_cart_page(self,checkout_page):
        checkout_page.click_on_cancel_button()
        checkout_page.should_back_to_cart_page()

    def test_error_message_is_disappeared(self,checkout_page):
        checkout_page.fill_form("","","")
        checkout_page.click_on_continue_button()
        checkout_page.click_on_close_error_button()
        checkout_page.should_error_message_disappear()

    def test_validation_icon_is_disappeared(self,checkout_page):
        checkout_page.fill_form("","","")
        checkout_page.click_on_continue_button()
        checkout_page.click_on_close_error_button()
        checkout_page.should_error_icon_disappear()

