from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from config import Credentials, URLs


class LoginPage(BasePage):
    def is_login_form_visible(self) -> bool:
        return self.is_element_visible(LoginPageLocators.USERNAME_FORM)

    def is_password_form_visible(self) -> bool:
        return self.is_element_visible(LoginPageLocators.PASSWORD_FORM)

    def is_error_notification_visible(self) -> bool:
        return self.is_element_visible(LoginPageLocators.ERROR_NOTIFICATION)

    def get_error_message(self) -> str:
        return self.get_text(LoginPageLocators.ERROR_NOTIFICATION)

    def login(self, username: str = Credentials.STANDARD_USER, password: str = Credentials.PASSWORD):
        self.input_text(LoginPageLocators.USERNAME_FORM, username)
        self.input_text(LoginPageLocators.PASSWORD_FORM, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def close_error_notification(self):
        self.click_element(LoginPageLocators.CLOSE_ERROR_BUTTON)

    def should_be_logged_in(self):
        assert self.is_login_form_visible()
        assert self.is_password_form_visible()
        self.login()
        assert self.get_current_url() == URLs.INVENTORY_URL

    def should_show_error_for_invalid_credentials(self, username: str = "invalid", password: str = "invalid"):
        self.login(username, password)
        assert self.is_error_notification_visible()
        error_text = self.get_error_message()
        assert "do not match any user" in error_text

    def should_close_error_notification(self):
        self.close_error_notification()
        assert self.is_element_disappeared(LoginPageLocators.ERROR_NOTIFICATION)

    def should_show_username_required_error(self):
        self.input_text(LoginPageLocators.PASSWORD_FORM, "somepassword")
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        error_text = self.get_error_message()
        assert "Username" in error_text

    def should_show_password_required_error(self):
        self.input_text(LoginPageLocators.USERNAME_FORM, "someuser")
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        error_text = self.get_error_message()
        assert "Password" in error_text
