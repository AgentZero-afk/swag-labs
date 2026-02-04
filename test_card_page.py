import pytest
from pages.card_page import CardPage
from conftest import get_cached_product_links
from config import URLs


@pytest.fixture
def card_page(logged_in_browser):
    return CardPage(logged_in_browser, URLs.INVENTORY_URL)


@pytest.mark.regression
class TestProductCard:
    def test_back_button_redirects_to_inventory(self, card_page):
        card_page.click_product_link()
        card_page.should_redirect_to_inventory()

    def test_product_card_displays_all_elements(self, card_page):
        card_page.click_product_link()
        card_page.should_display_complete_product_card()

    @pytest.mark.parametrize("product_link", get_cached_product_links())
    def test_each_product_card_displays_correctly(self, logged_in_browser, product_link):
        page = CardPage(logged_in_browser, product_link)
        page.browser.get(product_link)
        page.should_display_complete_product_card()
