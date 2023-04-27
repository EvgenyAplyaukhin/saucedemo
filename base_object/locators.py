from selenium.webdriver.common.by import By
class Locators:
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login-button')
    TITLE = (By.CLASS_NAME, 'title')
    ERROR = (By.CLASS_NAME, 'error-message-container')
    OPEN_MENU = (By.CLASS_NAME, 'bm-burger-button')
    LOGOUT = (By.ID, 'logout_sidebar_link')
    PRIMARY_BTN = (By.ID, 'add-to-cart-sauce-labs-backpack')
    CART_LINK = (By.CLASS_NAME, 'shopping_cart_badge')
    CHECKOUT = (By.ID, 'checkout')
    FIRST_NAME_FIELD = (By.ID, 'first-name')
    LAST_NAME_FIELD = (By.ID, 'last-name')
    POSTAL_COD_FIELD = (By.ID, 'postal-code')
    CONTINUE = (By.ID, 'continue')
    FINISH = (By.ID, 'finish')

