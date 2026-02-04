from pages.base_page import BasePage
from pages.locators import FooterLocators
from selenium.webdriver.support import expected_conditions as EC
from config import URLs


class FooterPage(BasePage):
    def click_twitter_link(self):
        self.click_element(FooterLocators.TWITTER_BUTTON)

    def click_facebook_link(self):
        self.click_element(FooterLocators.FACEBOOK_BUTTON)

    def click_linkedin_link(self):
        self.click_element(FooterLocators.LINKEDIN_BUTTON)

    def is_copyright_visible(self) -> bool:
        return self.is_element_visible(FooterLocators.COPYRIGHT_INFO)

    def click_on_social_link(self, click_method):
        click_method()
        self.switch_to_new_tab()

    def should_be_redirect_to_social_link(self, expected_url_part: str):
        self.wait.until(EC.url_contains(expected_url_part))
        assert expected_url_part in self.get_current_url(), f"Expected {expected_url_part} but got {self.get_current_url()}"

    def should_open_twitter(self):
        self.should_be_redirect_to_social_link("x.com/saucelabs")

    def should_open_facebook(self):
        self.should_be_redirect_to_social_link("facebook.com/saucelabs")

    def should_open_linkedin(self):
        self.should_be_redirect_to_social_link("linkedin.com/company/sauce-labs")

    def should_display_copyright(self):
        assert self.is_copyright_visible()
