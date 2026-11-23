from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CLASS_NAME, "icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    BASKET_PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "#messages .alert-success:nth-child(1) .alertinner strong",
    )
    BASKET_PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "#messages .alert-info .alertinner strong",
    )


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")
