from selenium.webdriver.common.by import By
class Locators:
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login-button')
    TITLE = (By.CLASS_NAME, 'title')
    ERROR = (By.CLASS_NAME, 'error-message-container')