from base_object.base import BaseObject
from base_object.locators import Locators

class IndexPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_username(self):
        self.enter_value(Locators.USERNAME_FIELD, 'standard_user')

    def enter_password(self):
        self.enter_value(Locators.PASSWORD_FIELD, 'secret_sauce')

    def click_to_login_btn(self):
        self.click(Locators.LOGIN_BTN)

    def check_title(self):
        expected_result = 'Products'
        actual_result = self.is_visible(Locators.TITLE).text
        self.check_equal(expected_result, actual_result)

    def enter_wrong_username(self):
        self.enter_value(Locators.USERNAME_FIELD, 'zhenya')

    def check_error_message_container(self):
        expected_result = 'Epic sadface: Username and password do not match any user in this service'
        actual_result = self.is_visible(Locators.ERROR).text
        self.check_equal(expected_result, actual_result)











