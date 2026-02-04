from pages.base_page import BasePage
from pages.locators import CheckoutPageLocators


class CheckoutPage(BasePage):
    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.input_text(CheckoutPageLocators.FIRST_NAME_INPUT, first_name)
        self.input_text(CheckoutPageLocators.LAST_NAME_INPUT, last_name)
        self.input_text(CheckoutPageLocators.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self):
        self.click_element(CheckoutPageLocators.CONTINUE_BUTTON)

    def click_cancel(self):
        self.click_element(CheckoutPageLocators.CANCEL_BUTTON)

    def click_finish(self):
        self.click_element(CheckoutPageLocators.FINISH_BUTTON)

    def is_order_complete(self) -> bool:
        return self.is_element_visible(CheckoutPageLocators.COMPLETE_HEADER)

    def should_complete_checkout(self, first_name: str, last_name: str, postal_code: str):
        self.fill_checkout_info(first_name, last_name, postal_code)
        self.click_continue()
        self.click_finish()
        assert self.is_order_complete()
