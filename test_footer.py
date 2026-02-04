import pytest
from pages.footer_page import FooterPage
from config import URLs


@pytest.fixture
def footer_page(logged_in_browser):
    return FooterPage(logged_in_browser, URLs.INVENTORY_URL)


@pytest.mark.regression
class TestFooter:
    def test_twitter_link_works(self, footer_page):
        footer_page.should_open_twitter()

    def test_facebook_link_works(self, footer_page):
        footer_page.should_open_facebook()

    def test_linkedin_link_works(self, footer_page):
        footer_page.should_open_linkedin()

    def test_copyright_is_displayed(self, footer_page):
        footer_page.should_display_copyright()
