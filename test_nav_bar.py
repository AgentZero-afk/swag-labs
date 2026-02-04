import pytest
from pages.nav_bar_page import NavBarPage
from config import URLs


@pytest.fixture
def nav_page(logged_in_browser):
    return NavBarPage(logged_in_browser, URLs.INVENTORY_URL)


@pytest.mark.navigation
class TestNavBar:
    def test_nav_menu_opens(self, nav_page):
        nav_page.open_nav_menu()
        assert nav_page.is_nav_menu_visible()

    def test_all_items_link_works(self, nav_page):
        nav_page.should_navigate_to_inventory()

    def test_about_link_works(self, nav_page):
        nav_page.should_navigate_to_about()

    def test_logout_works(self, nav_page):
        nav_page.should_logout_successfully()

    def test_nav_menu_closes(self, nav_page):
        nav_page.should_close_nav_menu()
