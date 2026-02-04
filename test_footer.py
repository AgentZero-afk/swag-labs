import pytest
from pages.footer_page import FooterPage
from config import URLs


@pytest.fixture
def footer_page(logged_in_browser):
    return FooterPage(logged_in_browser, URLs.INVENTORY_URL)


@pytest.mark.regression
class TestFooter:
    def test_twitter_link_works(self, footer_page):
        footer_page.click_on_social_link(footer_page.click_twitter_link)
        footer_page.should_open_twitter()
        footer_page.close_tab_and_switch_back()

    def test_facebook_link_works(self, footer_page):
        footer_page.click_on_social_link(footer_page.click_facebook_link)
        footer_page.should_open_facebook()
        footer_page.close_tab_and_switch_back()

    def test_linkedin_link_works(self, footer_page):
        footer_page.click_on_social_link(footer_page.click_linkedin_link)
        footer_page.should_open_linkedin()
        footer_page.close_tab_and_switch_back()

    def test_copyright_is_displayed(self, footer_page):
        footer_page.should_display_copyright()
