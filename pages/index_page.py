from base_object.base import BaseObject
from base_object.locators import Locators
from support.assertions import Assertions


class IndexPage(BaseObject, Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_username(self):
        self.enter_value(Locators.USERNAME_FIELD, 'standard_user')

    def enter_password(self, password):
        self.enter_value(Locators.PASSWORD_FIELD, password)

    def click_to_login_btn(self):
        self.click(Locators.LOGIN_BTN)

    def click_to_bm_burger_button(self):
        self.click(Locators.OPEN_MENU)

    def click_to_logout_sidebar_link(self):
        self.click(Locators.LOGOUT)

    def check_title(self):
        expected_result = 'Products'
        actual_result = self.is_visible(Locators.TITLE).text
        self.check_equal(expected_result, actual_result)

    def enter_wrong_username(self, username):
        self.enter_value(Locators.USERNAME_FIELD, username)

    def check_error_message_container(self, error_message):
        actual_result = self.is_visible(Locators.ERROR).text
        self.check_equal(error_message, actual_result)











