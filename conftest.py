import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from config import URLs, Credentials, Timeouts, VALID_USERS
from pages.locators import LoginPageLocators


def _get_chrome_options(headless: bool = False) -> Options:
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })
    if headless:
        chrome_options.add_argument("--headless")
    return chrome_options


def _login(driver, username: str = Credentials.STANDARD_USER, password: str = Credentials.PASSWORD):
    driver.find_element(*LoginPageLocators.USERNAME_FORM).send_keys(username)
    driver.find_element(*LoginPageLocators.PASSWORD_FORM).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()


def get_product_links() -> list[str]:
    driver = webdriver.Chrome(options=_get_chrome_options(headless=True))
    driver.implicitly_wait(Timeouts.IMPLICIT_WAIT)

    try:
        driver.get(URLs.BASE_URL)
        _login(driver)

        elements = driver.find_elements(By.CSS_SELECTOR, "[data-test$='-title-link']")
        links = []
        for element in elements:
            element_id = element.get_attribute("id")
            product_id = element_id.split("_")[1]
            links.append(URLs.ITEM_URL_TEMPLATE.format(product_id))
        return links
    finally:
        driver.quit()


@pytest.fixture
def browser():
    driver = webdriver.Chrome(options=_get_chrome_options())
    driver.maximize_window()
    driver.implicitly_wait(Timeouts.IMPLICIT_WAIT)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_browser(browser):
    browser.get(URLs.BASE_URL)
    _login(browser)
    return browser


@pytest.fixture(params=VALID_USERS)
def valid_user(request):
    return {"username": request.param[0], "password": request.param[1]}


_product_links_cache = None


def get_cached_product_links() -> list[str]:
    global _product_links_cache
    if _product_links_cache is None:
        _product_links_cache = get_product_links()
    return _product_links_cache


@pytest.fixture
def product_links():
    return get_cached_product_links()
