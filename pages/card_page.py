from pages.base_page import BasePage
from pages.locators import CardPageLocators, MainPageLocators
from config import URLs


class CardPage(BasePage):
    def is_product_card_complete(self) -> bool:
        return all([
            self.is_element_visible(CardPageLocators.NAME_ITEM),
            self.is_element_visible(CardPageLocators.DESCRIPTION_ITEM),
            self.is_element_visible(CardPageLocators.PRICE_ITEM),
            self.is_element_visible(CardPageLocators.IMG_ITEM),
            self.is_element_visible(CardPageLocators.ADD_TO_CART_BUTTON)
        ])

    def click_product_link(self):
        self.click_element(MainPageLocators.ITEM_LINK)

    def click_back_to_products(self):
        self.click_element(CardPageLocators.BACK_TO_PRODUCTS_BUTTON)

    def get_product_name(self) -> str:
        return self.get_text(CardPageLocators.NAME_ITEM)

    def get_product_price(self) -> str:
        return self.get_text(CardPageLocators.PRICE_ITEM)

    def get_product_description(self) -> str:
        return self.get_text(CardPageLocators.DESCRIPTION_ITEM)

    def add_to_cart(self):
        self.click_element(CardPageLocators.ADD_TO_CART_BUTTON)

    def should_display_complete_product_card(self):
        assert self.is_product_card_complete()

    def should_redirect_to_inventory(self):
        self.click_back_to_products()
        assert self.get_current_url() == URLs.INVENTORY_URL
