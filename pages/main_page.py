from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.support.ui import Select
from config import URLs


class MainPage(BasePage):
    def get_prices(self) -> list[float]:
        price_elements = self.get_elements(MainPageLocators.ITEM_PRICE)
        return [float(el.text.replace("$", "")) for el in price_elements]

    def get_product_names(self) -> list[str]:
        name_elements = self.get_elements(MainPageLocators.ITEM_NAME)
        return [el.text for el in name_elements]

    def select_sort_option(self, value: str):
        dropdown = self.browser.find_element(*MainPageLocators.SELECT_FILTER)
        Select(dropdown).select_by_value(value)

    def add_to_cart(self):
        self.click_element(MainPageLocators.ADD_TO_CART_BUTTON)

    def remove_from_cart(self):
        self.click_element(MainPageLocators.REMOVE_FROM_CART_BUTTON)

    def add_multiple_items_to_cart(self, count: int = 3):
        buttons = self.get_elements(MainPageLocators.ADD_TO_CART_BUTTONS)
        for button in buttons[:count]:
            button.click()

    def get_cart_badge_count(self) -> str:
        return self.get_text(MainPageLocators.SHOPPING_CART_BADGE)

    def is_cart_badge_visible(self) -> bool:
        return self.is_element_visible(MainPageLocators.SHOPPING_CART_BADGE)

    def click_product_link(self):
        self.click_element(MainPageLocators.ITEM_LINK)

    def sort_by_price_high_to_low(self):
        self.select_sort_option("hilo")

    def should_be_sorted_by_price_high_to_low(self):
        prices = self.get_prices()
        assert prices == sorted(prices, reverse=True), f"Expected sorted hi-lo"

    def sort_by_price_low_to_high(self):
        self.select_sort_option("lohi")

    def should_be_sorted_by_price_low_to_high(self):
        prices = self.get_prices()
        assert prices == sorted(prices), f"Expected sorted lo-hi"

    def sort_by_name_z_to_a(self):
        self.select_sort_option("za")

    def should_be_sorted_by_name_z_to_a(self):
        names = self.get_product_names()
        assert names == sorted(names, reverse=True), f"Expected sorted z-a"

    def sort_by_name_a_to_z(self):
        self.select_sort_option("az")

    def should_be_sorted_by_name_a_to_z(self):
        names = self.get_product_names()
        assert names == sorted(names), f"Expected sorted a-z"

    def should_show_badge_after_add_to_cart(self):
        assert self.is_cart_badge_visible(), f"After adding to cart, cart_badge is should be visible"

    def should_hide_badge_after_remove_from_cart(self):
        assert self.is_element_disappeared(MainPageLocators.SHOPPING_CART_BADGE), f"After remove all items from cart, cart_badge is not disappeared."

    def should_have_cart_count(self, expected_count: str):
        assert self.get_cart_badge_count() == expected_count, f"Expected {expected_count} but got {self.get_cart_badge_count()}"

    def should_redirect_to_product_page(self, product_id: str):
        assert URLs.ITEM_URL_TEMPLATE.format(product_id) == self.get_current_url(), f"Expected {URLs.ITEM_URL_TEMPLATE.format(product_id)} got {self.get_current_url()}"

    def go_to_cart(self):
        self.click_element(MainPageLocators.SHOPPING_CART_LINK)

    def get_product_desc(self) -> list[str]:
        desc_elements = self.get_elements(MainPageLocators.ITEM_DESCRIPTION)
        return [el.text for el in desc_elements]

    def get_product_prices_text(self) -> list[str]:
        price_elements = self.get_elements(MainPageLocators.ITEM_PRICE)
        return [el.text for el in price_elements]
