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

    def verify_social_link(self, click_method, expected_url_part: str):
        click_method()
        self.switch_to_new_tab()
        self.wait.until(EC.url_contains(expected_url_part))
        assert expected_url_part in self.get_current_url()
        self.close_tab_and_switch_back()
        self.browser.get(URLs.INVENTORY_URL)

    def should_open_twitter(self):
        self.verify_social_link(self.click_twitter_link, "x.com/saucelabs")

    def should_open_facebook(self):
        self.verify_social_link(self.click_facebook_link, "facebook.com/saucelabs")

    def should_open_linkedin(self):
        self.verify_social_link(self.click_linkedin_link, "linkedin.com/company/sauce-labs")

    def should_display_copyright(self):
        assert self.is_copyright_visible()
