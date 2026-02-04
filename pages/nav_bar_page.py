from pages.base_page import BasePage
from pages.locators import NavBarLocators
from config import URLs


class NavBarPage(BasePage):
    def open_nav_menu(self):
        self.click_element(NavBarLocators.NAV_BAR_BUTTON)

    def close_nav_menu(self):
        self.click_element(NavBarLocators.CLOSE_NAV_BUTTON)

    def click_all_items(self):
        self.click_element(NavBarLocators.ALL_ITEMS_NAV_BUTTON)

    def click_about(self):
        self.click_element(NavBarLocators.ABOUT_NAV_BUTTON)

    def click_logout(self):
        self.click_element(NavBarLocators.LOGOUT_NAV_BUTTON)

    def is_nav_menu_visible(self) -> bool:
        return self.is_element_visible(NavBarLocators.NAV_BAR_LIST)

    def should_display_nav_menu(self):
        assert self.is_nav_menu_visible(), f"Expected nav menu to be visible"

    def go_to_product(self, product_id: str):
        self.browser.get(URLs.ITEM_URL_TEMPLATE.format(product_id))

    def should_navigate_to_inventory(self):
        assert self.get_current_url() == URLs.INVENTORY_URL, f"Expected {URLs.INVENTORY_URL} got {self.get_current_url()}"

    def should_navigate_to_about(self):
        assert self.get_current_url() == URLs.ABOUT_URL, f"Expected {URLs.ABOUT_URL}, got {self.get_current_url()}"

    def should_logout_successfully(self):
        assert self.get_current_url() == URLs.BASE_URL, f"Expected {URLs.BASE_URL} got {self.get_current_url()}"

    def should_close_nav_menu(self):
        assert self.is_element_disappeared(NavBarLocators.NAV_BAR_LIST), f"Nav-menu is not disappeared"
