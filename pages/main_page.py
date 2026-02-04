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

    def should_be_sorted_by_price_high_to_low(self):
        self.select_sort_option("hilo")
        prices = self.get_prices()
        assert prices == sorted(prices, reverse=True)

    def should_be_sorted_by_price_low_to_high(self):
        self.select_sort_option("lohi")
        prices = self.get_prices()
        assert prices == sorted(prices)

    def should_be_sorted_by_name_z_to_a(self):
        self.select_sort_option("za")
        names = self.get_product_names()
        assert names == sorted(names, reverse=True)

    def should_be_sorted_by_name_a_to_z(self):
        self.select_sort_option("az")
        names = self.get_product_names()
        assert names == sorted(names)

    def should_show_badge_after_add_to_cart(self):
        self.add_to_cart()
        assert self.is_cart_badge_visible()

    def should_hide_badge_after_remove_from_cart(self):
        self.add_to_cart()
        self.remove_from_cart()
        assert self.is_element_disappeared(MainPageLocators.SHOPPING_CART_BADGE)

    def should_update_cart_count_correctly(self):
        self.add_multiple_items_to_cart(3)
        assert self.get_cart_badge_count() == "3"
        self.remove_from_cart()
        assert self.get_cart_badge_count() == "2"

    def should_redirect_to_product_page(self):
        self.click_product_link()
        assert URLs.ITEM_URL_TEMPLATE.format("4") == self.get_current_url()
