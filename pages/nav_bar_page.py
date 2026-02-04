from pages.base_page import BasePage
from pages.locators import NavBarLocators
from config import URLs


class NavBarPage(BasePage):
    def open_nav_menu(self):
        self.click_element(NavBarLocators.NAV_BAR_BUTTON)

    def close_nav_menu(self):
        self.click_element(NavBarLocators.CLOSE_NAV_BUTTON)

    def click_all_items(self):
        self.open_nav_menu()
        self.click_element(NavBarLocators.ALL_ITEMS_NAV_BUTTON)

    def click_about(self):
        self.open_nav_menu()
        self.click_element(NavBarLocators.ABOUT_NAV_BUTTON)

    def click_logout(self):
        self.open_nav_menu()
        self.click_element(NavBarLocators.LOGOUT_NAV_BUTTON)

    def is_nav_menu_visible(self) -> bool:
        return self.is_element_visible(NavBarLocators.NAV_BAR_LIST)

    def should_navigate_to_inventory(self):
        self.browser.get(URLs.ITEM_URL_TEMPLATE.format("4"))
        self.click_all_items()
        assert self.get_current_url() == URLs.INVENTORY_URL

    def should_navigate_to_about(self):
        self.click_about()
        assert self.get_current_url() == URLs.ABOUT_URL

    def should_logout_successfully(self):
        self.click_logout()
        assert self.get_current_url() == URLs.BASE_URL

    def should_close_nav_menu(self):
        self.open_nav_menu()
        self.close_nav_menu()
        assert self.is_element_disappeared(NavBarLocators.NAV_BAR_LIST)
