import pytest

from pages.login_page import LoginPage
from config import URLs


@pytest.fixture
def login_page(browser):
    page = LoginPage(browser, URLs.BASE_URL)
    page.open()
    return page


@pytest.mark.smoke
@pytest.mark.login
class TestLogin:
    def test_successful_login(self, login_page):
        login_page.should_be_login_form()
        login_page.login()
        login_page.should_be_logged_in()

    def test_all_valid_users_can_login(self, login_page, valid_user):
        login_page.login(valid_user["username"], valid_user["password"])
        login_page.should_be_logged_in()

    def test_all_invalid_users_cannot_login(self, login_page, invalid_user):
        login_page.login(invalid_user["username"], invalid_user["password"])
        login_page.should_be_ban_user_error()



@pytest.mark.login
class TestLoginErrors:
    def test_invalid_credentials_show_error(self, login_page):
        login_page.login("invalid", "invalid")
        login_page.should_show_error_for_invalid_credentials()

    def test_error_notification_can_be_closed(self, login_page):
        login_page.login("invalid", "invalid")
        login_page.close_error_notification()
        login_page.should_close_error_notification()

    def test_empty_username_shows_error(self, login_page):
        login_page.login_without_username()
        login_page.should_show_username_required_error()

    def test_empty_password_shows_error(self, login_page):
        login_page.login_without_password()
        login_page.should_show_password_required_error()
