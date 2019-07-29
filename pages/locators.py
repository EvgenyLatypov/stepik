from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    GO_TO_CART = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRMATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(),'Your basket now qualifies for the')]")


class OtherLocators(object):
    QUIZ_ANSWER = (By.CSS_SELECTOR, "textarea.textarea")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.submit-submission")
    LOG_IN = (By.CSS_SELECTOR, ".navbar__auth_type_login")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login_email")
    LOGIN_PASSWORD = (By.ID, "id_login_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".button_with-loader")
    ATTEMPT_MESSAGE = (By.CSS_SELECTOR, "div.attempt__message")


class CartLocators(object):
    PRODUCT_NAME = (By.XPATH, "//a[contains(text(),'The City and the Stars')]")
    EMPTY_CART_MESSAGE = (By.XPATH, "//p[contains(text(),'Your basket is empty.')]")
