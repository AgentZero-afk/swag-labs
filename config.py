class URLs:
    BASE_URL = "https://www.saucedemo.com/"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
    CART_URL = "https://www.saucedemo.com/cart.html"
    CHECKOUT_URL = "https://www.saucedemo.com/checkout-step-one.html"
    ITEM_URL_TEMPLATE = "https://www.saucedemo.com/inventory-item.html?id={}"
    ABOUT_URL = "https://saucelabs.com/"


class Credentials:
    STANDARD_USER = "standard_user"
    LOCKED_OUT_USER = "locked_out_user"
    PROBLEM_USER = "problem_user"
    PERFORMANCE_GLITCH_USER = "performance_glitch_user"
    ERROR_USER = "error_user"
    VISUAL_USER = "visual_user"
    PASSWORD = "secret_sauce"


class Timeouts:
    IMPLICIT_WAIT = 5
    EXPLICIT_WAIT = 10


VALID_USERS = [
    (Credentials.STANDARD_USER, Credentials.PASSWORD),
    (Credentials.PROBLEM_USER, Credentials.PASSWORD),
    (Credentials.PERFORMANCE_GLITCH_USER, Credentials.PASSWORD),
    (Credentials.ERROR_USER, Credentials.PASSWORD),
    (Credentials.VISUAL_USER, Credentials.PASSWORD),
]

INVALID_USERS = [
    (Credentials.LOCKED_OUT_USER, Credentials.PASSWORD)
]
