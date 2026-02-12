from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FORM = (By.CSS_SELECTOR, "input[data-test='username']")
    PASSWORD_FORM = (By.CSS_SELECTOR, "input[data-test='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[id='login-button']")
    ERROR_NOTIFICATION = (By.CSS_SELECTOR, ".error-message-container h3[data-test='error']")
    CLOSE_ERROR_BUTTON = (By.CSS_SELECTOR, "button[data-test='error-button']")


class MainPageLocators:
    SELECT_FILTER = (By.CSS_SELECTOR, "select[data-test='product-sort-container']")
    ITEM_PRICE = (By.CSS_SELECTOR, "div[data-test='inventory-item-price']")
    ITEM_NAME = (By.CSS_SELECTOR, "div[data-test='inventory-item-name']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    REMOVE_FROM_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test='remove-sauce-labs-backpack']")
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, "span[data-test='shopping-cart-badge']")
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    ITEM_LINK = (By.CSS_SELECTOR, "a[id='item_4_title_link']")
    ALL_ITEMS = (By.CSS_SELECTOR, "div[data-test='inventory-item-name']")
    ITEM_DESCRIPTION = (By.CSS_SELECTOR, "div[data-test='inventory-item-desc']")


class CardPageLocators:
    NAME_ITEM = (By.CSS_SELECTOR, "div[data-test='inventory-item-name']")
    DESCRIPTION_ITEM = (By.CSS_SELECTOR, "div[data-test='inventory-item-desc']")
    PRICE_ITEM = (By.CSS_SELECTOR, "div[data-test='inventory-item-price']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test='add-to-cart']")
    REMOVE_FROM_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test='remove']")
    IMG_ITEM = (By.CSS_SELECTOR, "img.inventory_details_img")
    BACK_TO_PRODUCTS_BUTTON = (By.CSS_SELECTOR, "button[data-test='back-to-products']")


class NavBarLocators:
    NAV_BAR_BUTTON = (By.CSS_SELECTOR, "button[id='react-burger-menu-btn']")
    NAV_BAR_LIST = (By.CSS_SELECTOR, "nav[class='bm-item-list']")
    ALL_ITEMS_NAV_BUTTON = (By.CSS_SELECTOR, "a[id='inventory_sidebar_link']")
    ABOUT_NAV_BUTTON = (By.CSS_SELECTOR, "a[id='about_sidebar_link']")
    LOGOUT_NAV_BUTTON = (By.CSS_SELECTOR, "a[id='logout_sidebar_link']")
    CLOSE_NAV_BUTTON = (By.CSS_SELECTOR, "button[id='react-burger-cross-btn']")


class FooterLocators:
    TWITTER_BUTTON = (By.CSS_SELECTOR, "a[data-test='social-twitter']")
    FACEBOOK_BUTTON = (By.CSS_SELECTOR, "a[data-test='social-facebook']")
    LINKEDIN_BUTTON = (By.CSS_SELECTOR, "a[data-test='social-linkedin']")
    COPYRIGHT_INFO = (By.CSS_SELECTOR, "div[data-test='footer-copy']")


class CartPageLocators:
    CART_ITEM = (By.CSS_SELECTOR, "div[data-test='inventory-item-name']")
    CART_ITEM_LINK = (By.CSS_SELECTOR, "a[data-test^='item-'][data-test$='-title-link']")
    DESCRIPTION_ITEM_CART = (By.CSS_SELECTOR, "div[data-test='inventory-item-desc']")
    PRICE_ITEM_CART = (By.CSS_SELECTOR, "div[data-test='inventory-item-price']")
    REMOVE_ITEM_FROM_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test^='remove-']")
    BACK_TO_ITEM_LIST_BUTTON = (By.CSS_SELECTOR, "button[data-test='continue-shopping']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[data-test='checkout']")
    CART_QUANTITY = (By.CSS_SELECTOR, "div[data-test='item-quantity']")


class CheckoutPageLocators:
    CANCEL_BUTTON = (By.CSS_SELECTOR, "button[data-test='cancel']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[data-test='continue']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-test='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-test='lastName']")
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "input[data-test='postalCode']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    ERROR_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[data-test='error-button']")
    VALIDATION_ICON = (By.CSS_SELECTOR, "svg[data-icon='times-circle']")


