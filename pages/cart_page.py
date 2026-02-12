from pages.base_page import BasePage
from pages.locators import CartPageLocators
from config import URLs


class CartPage(BasePage):

    def remove_from_cart(self):
        self.click_element(CartPageLocators.REMOVE_ITEM_FROM_CART_BUTTON)

    def remove_items_from_cart(self):
        while self.get_elements(CartPageLocators.REMOVE_ITEM_FROM_CART_BUTTON):
            self.click_element(CartPageLocators.REMOVE_ITEM_FROM_CART_BUTTON)

    def should_item_removed_from_cart(self):
        assert self.is_element_disappeared(CartPageLocators.CART_ITEM), f"Expected cart item was removed from cart page"

    def back_to_item_list(self):
        self.click_element(CartPageLocators.BACK_TO_ITEM_LIST_BUTTON)

    def should_be_back_to_item_list(self):
        assert self.get_current_url() == URLs.INVENTORY_URL, f"Expected inventory page, got {self.get_current_url()}"

    def go_to_checkout(self):
        self.click_element(CartPageLocators.CHECKOUT_BUTTON)

    def should_redirect_to_checkout(self):
        assert self.get_current_url() == URLs.CHECKOUT_URL, f"Expected checkout page, got {self.get_current_url()}"


    def should_redirect_to_item_page(self,product_id: str):
        assert URLs.ITEM_URL_TEMPLATE.format(product_id) == self.get_current_url(), f"Expected {URLs.ITEM_URL_TEMPLATE.format(product_id)} got {self.get_current_url()}"


    def should_description_visible(self):
        assert self.is_element_visible(CartPageLocators.DESCRIPTION_ITEM_CART), f"Expected description visible on page"

    def should_price_visible(self):
        assert self.is_element_visible(CartPageLocators.PRICE_ITEM_CART), f"Expected price visible on page"

    def should_item_title_visible(self):
        assert self.is_element_visible(CartPageLocators.CART_ITEM), f"Expected item title visible on page"

    def click_on_item(self):
        self.click_element(CartPageLocators.CART_ITEM_LINK)

    def get_item_name(self):
        return self.get_text(CartPageLocators.CART_ITEM)

    def get_item_price(self):
        return self.get_text(CartPageLocators.PRICE_ITEM_CART)

    def get_item_description(self):
        return self.get_text(CartPageLocators.DESCRIPTION_ITEM_CART)

    def get_cart_items_count(self):
        return len(self.get_elements(CartPageLocators.CART_ITEM))

    def should_cart_items_eq_add_items_data(self, expected_name: str, expected_price: str, expected_desc: str):
        assert self.get_item_name() == expected_name, f"Expected {expected_name}, got {self.get_item_name()}"
        assert self.get_item_price() == expected_price, f"Expected {expected_price}, got {self.get_item_price()}"
        assert self.get_item_description() == expected_desc, f"Expected {expected_desc}, got {self.get_item_description()}"


    def should_cart_items_count_eq(self,expected_count: int):
        assert self.get_cart_items_count() == expected_count, f"Expected {expected_count}, got {self.get_cart_items_count()}"

    def should_quantity_visible(self):
        assert self.is_element_visible(CartPageLocators.CART_QUANTITY), f"Expected cart quantity visible on page"

    def get_all_item_names(self) -> list:
        elements = self.get_elements(CartPageLocators.CART_ITEM)
        return [el.text for el in elements]

    def should_remove_but_still_in_cart(self,names_before: list, removed_name: str, names_after: list):
        assert removed_name not in names_after, f"{removed_name}, should be removed from cart"
        assert names_after == names_before[1:], f"Remaining items changed. Expected {names_before[1:]}, got {names_after}"
