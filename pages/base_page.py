from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from config import Timeouts


class BasePage:
    def __init__(self, browser: WebDriver, url: str):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(self.browser, Timeouts.EXPLICIT_WAIT)

    def open(self):
        self.browser.get(self.url)

    def click_element(self, locator: tuple):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator: tuple, text: str):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    def clear_and_input_text(self, locator: tuple, text: str):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_element_visible(self, locator: tuple) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_disappeared(self, locator: tuple) -> bool:
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_current_url(self) -> str:
        return self.browser.current_url

    def get_elements(self, locator: tuple) -> list:
        return self.browser.find_elements(*locator)

    def switch_to_new_tab(self):
        original_window = self.browser.current_window_handle
        self.wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
                break

    def close_tab_and_switch_back(self):
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])
