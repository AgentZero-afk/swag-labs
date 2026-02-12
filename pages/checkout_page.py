from pages.base_page import BasePage
from pages.locators import CheckoutPageLocators
from config import URLs

class CheckoutPage(BasePage):

    def fill_form(self,first_name: str,last_name: str,postal_code: str):
        if first_name:
            self.input_text(CheckoutPageLocators.FIRST_NAME_INPUT, first_name)
        if last_name:
            self.input_text(CheckoutPageLocators.LAST_NAME_INPUT, last_name)
        if postal_code:
            self.input_text(CheckoutPageLocators.POSTAL_CODE_INPUT, postal_code)

    def should_show_error(self,expected_text: str):
        error = self.get_text(CheckoutPageLocators.ERROR_MESSAGE)
        assert expected_text == error, f"Expected '{expected_text}' but got '{error}'"



    def click_on_continue_button(self):
        self.click_element(CheckoutPageLocators.CONTINUE_BUTTON)

    def click_on_cancel_button(self):
        self.click_element(CheckoutPageLocators.CANCEL_BUTTON)

    def should_go_to_checkout_page_step_two(self):
        assert self.get_current_url() == URLs.CHECKOUT_STEP_TWO_URL, f"Expected https://www.saucedemo.com/checkout-step-two.html but got {self.get_current_url()}"

    def should_back_to_cart_page(self):
        assert self.get_current_url() == URLs.CART_URL, f"Expected https://www.saucedemo.com/cart.html, but got {self.get_current_url()}"

    def click_on_close_error_button(self):
        self.click_element(CheckoutPageLocators.ERROR_CLOSE_BUTTON)

    def should_error_message_disappear(self):
        assert self.is_element_disappeared(CheckoutPageLocators.ERROR_MESSAGE), f"Error message is not disappeared"

    def should_error_icon_disappear(self):
        assert self.is_element_disappeared(CheckoutPageLocators.VALIDATION_ICON), f"Error icon is not disappeared"

