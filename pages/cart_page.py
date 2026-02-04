from pages.base_page import BasePage
from pages.locators import CartPageLocators
from config import URLs


class CartPage(BasePage):
    def get_cart_items(self) -> list:
        return self.get_elements(CartPageLocators.CART_ITEM)

    def get_cart_item_count(self) -> int:
        return len(self.get_cart_items())

    def click_checkout(self):
        self.click_element(CartPageLocators.CHECKOUT_BUTTON)

    def click_continue_shopping(self):
        self.click_element(CartPageLocators.CONTINUE_SHOPPING_BUTTON)

    def remove_item(self):
        self.click_element(CartPageLocators.REMOVE_BUTTON)

    def should_have_items(self, expected_count: int):
        actual_count = self.get_cart_item_count()
        assert actual_count == expected_count

    def should_be_empty(self):
        self.should_have_items(0)

    def should_redirect_to_checkout(self):
        self.click_checkout()
        assert self.get_current_url() == URLs.CHECKOUT_URL

    def should_redirect_to_inventory(self):
        self.click_continue_shopping()
        assert self.get_current_url() == URLs.INVENTORY_URL
