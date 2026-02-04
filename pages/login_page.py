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
        assert self.get_current_url() == URLs.INVENTORY_URL, f"Expected {URLs.INVENTORY_URL}, got {self.get_current_url()}"

    def should_be_login_form(self):
        assert self.is_login_form_visible(), f"Expected visible login form, got invisible"
        assert self.is_password_form_visible(), f"Expected visible password form, got invisible"

    def should_show_error_for_invalid_credentials(self):
        assert self.is_error_notification_visible()
        error_text = self.get_error_message()
        assert "do not match any user" in error_text, f"Expected 'do not match any user' in {error_text}"


    def should_be_ban_user_error(self):
        assert self.is_error_notification_visible(), f"Expected error notification visible, got invisible"

    def should_close_error_notification(self):
        assert self.is_element_disappeared(LoginPageLocators.ERROR_NOTIFICATION), f"Expected error notification disappeared, got not disappeared"

    def login_without_username(self, password: str = "somepassword"):
        self.input_text(LoginPageLocators.PASSWORD_FORM, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def login_without_password(self, username: str = "somename"):
        self.input_text(LoginPageLocators.USERNAME_FORM, username)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def should_show_username_required_error(self):
        error_text = self.get_error_message()
        assert "Username" in error_text, f"Expected 'Username' in {error_text}"

    def should_show_password_required_error(self):
        error_text = self.get_error_message()
        assert "Password" in error_text, f"Expected 'Password' in {error_text}"
