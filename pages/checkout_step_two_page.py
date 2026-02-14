from pages.base_page import BasePage
from pages.locators import CheckoutStepTwoPageLocators, CartPageLocators
from config import URLs


class CheckoutStepTwoPage(BasePage):

    def get_item_name(self):
        return self.get_text(CartPageLocators.CART_ITEM)

    def get_item_price(self):
        return self.get_text(CartPageLocators.PRICE_ITEM_CART)

    def get_item_description(self):
        return self.get_text(CartPageLocators.DESCRIPTION_ITEM_CART)

    def get_cart_items_count(self):
        return len(self.get_elements(CartPageLocators.CART_ITEM))

    def get_all_item_names(self) -> list:
        elements = self.get_elements(CartPageLocators.CART_ITEM)
        return [el.text for el in elements]

    def should_item_title_visible(self):
        assert self.is_element_visible(CartPageLocators.CART_ITEM), "Expected item title visible on page"

    def should_description_visible(self):
        assert self.is_element_visible(CartPageLocators.DESCRIPTION_ITEM_CART), "Expected description visible on page"

    def should_price_visible(self):
        assert self.is_element_visible(CartPageLocators.PRICE_ITEM_CART), "Expected price visible on page"

    def should_quantity_visible(self):
        assert self.is_element_visible(CartPageLocators.CART_QUANTITY), "Expected cart quantity visible on page"

    def should_cart_items_count_eq(self, expected_count: int):
        assert self.get_cart_items_count() == expected_count, f"Expected {expected_count}, got {self.get_cart_items_count()}"

    def should_cart_items_eq_added_data(self, expected_name: str, expected_price: str, expected_desc: str):
        assert self.get_item_name() == expected_name, f"Expected {expected_name}, got {self.get_item_name()}"
        assert self.get_item_price() == expected_price, f"Expected {expected_price}, got {self.get_item_price()}"
        assert self.get_item_description() == expected_desc, f"Expected {expected_desc}, got {self.get_item_description()}"

    def click_finish(self):
        self.click_element(CheckoutStepTwoPageLocators.FINISH_BUTTON)

    def click_cancel(self):
        self.click_element(CheckoutStepTwoPageLocators.CANCEL_BUTTON)

    def should_payment_info_visible(self):
        assert self.is_element_visible(CheckoutStepTwoPageLocators.PAYMENT_INFO_VALUE), "Expected payment info visible"

    def should_shipping_info_visible(self):
        assert self.is_element_visible(CheckoutStepTwoPageLocators.SHIPPING_INFO_VALUE), "Expected shipping info visible"

    def get_payment_info(self):
        return self.get_text(CheckoutStepTwoPageLocators.PAYMENT_INFO_VALUE)

    def get_shipping_info(self):
        return self.get_text(CheckoutStepTwoPageLocators.SHIPPING_INFO_VALUE)

    def get_subtotal(self):
        return self.get_text(CheckoutStepTwoPageLocators.PRICE_ITEM_INFO_VALUE)

    def get_tax(self):
        return self.get_text(CheckoutStepTwoPageLocators.PRICE_ITEM_TAX_VALUE)

    def get_total(self):
        return self.get_text(CheckoutStepTwoPageLocators.PRICE_ITEM_TOTAL_VALUE)

    def should_subtotal_visible(self):
        assert self.is_element_visible(CheckoutStepTwoPageLocators.PRICE_ITEM_INFO_VALUE), "Expected subtotal visible"

    def should_tax_visible(self):
        assert self.is_element_visible(CheckoutStepTwoPageLocators.PRICE_ITEM_TAX_VALUE), "Expected tax visible"

    def should_total_visible(self):
        assert self.is_element_visible(CheckoutStepTwoPageLocators.PRICE_ITEM_TOTAL_VALUE), "Expected total visible"

    def should_redirect_to_checkout_complete(self):
        assert "checkout-complete" in self.get_current_url(), f"Expected checkout-complete page, got {self.get_current_url()}"

    def should_redirect_to_inventory(self):
        assert self.get_current_url() == URLs.INVENTORY_URL, f"Expected {URLs.INVENTORY_URL}, got {self.get_current_url()}"

    def get_quantity(self):
        return self.get_text(CartPageLocators.CART_QUANTITY)

    def get_all_item_prices(self) -> list:
        elements = self.get_elements(CartPageLocators.PRICE_ITEM_CART)
        return [el.text for el in elements]

    def get_all_item_descriptions(self) -> list:
        elements = self.get_elements(CartPageLocators.DESCRIPTION_ITEM_CART)
        return [el.text for el in elements]

    def click_item_link(self):
        self.click_element(CartPageLocators.CART_ITEM_LINK)

    def parse_price(self, text: str) -> float:
        return float(text.split('$')[-1])

    def get_subtotal_value(self) -> float:
        return self.parse_price(self.get_subtotal())

    def get_tax_value(self) -> float:
        return self.parse_price(self.get_tax())

    def get_total_value(self) -> float:
        return self.parse_price(self.get_total())

    def get_all_item_prices_values(self) -> list[float]:
        return [self.parse_price(p) for p in self.get_all_item_prices()]

    def should_total_eq_subtotal_plus_tax(self):
        subtotal = self.get_subtotal_value()
        tax = self.get_tax_value()
        total = self.get_total_value()
        expected = round(subtotal + tax, 2)
        assert total == expected, f"Expected total {expected}, got {total} (subtotal={subtotal}, tax={tax})"

    def should_subtotal_eq_sum_of_prices(self):
        subtotal = self.get_subtotal_value()
        prices_sum = round(sum(self.get_all_item_prices_values()), 2)
        assert subtotal == prices_sum, f"Expected subtotal {prices_sum}, got {subtotal}"

    def should_quantity_eq(self, expected: str):
        actual = self.get_quantity()
        assert actual == expected, f"Expected quantity '{expected}', got '{actual}'"

    def should_payment_info_not_empty(self):
        info = self.get_payment_info()
        assert info, "Payment info is empty"

    def should_shipping_info_not_empty(self):
        info = self.get_shipping_info()
        assert info, "Shipping info is empty"

    def should_all_items_match(self, expected_names: list, expected_prices: list):
        actual_names = self.get_all_item_names()
        actual_prices = self.get_all_item_prices()
        assert actual_names == expected_names, f"Expected names {expected_names}, got {actual_names}"
        assert actual_prices == expected_prices, f"Expected prices {expected_prices}, got {actual_prices}"

    def should_redirect_to_item_page(self):
        assert "inventory-item.html" in self.get_current_url(), f"Expected item page, got {self.get_current_url()}"