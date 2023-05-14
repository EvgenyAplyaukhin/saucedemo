from base_object.base import BaseObject
from base_object.locators import Locators
from support.assertions import Assertions
import allure
from config import USERNAME


class IndexPage(BaseObject, Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('enter username')
    def enter_username(self):
        self.enter_value(Locators.USERNAME_FIELD, USERNAME)

    @allure.step('enter password')
    def enter_password(self, password):
        self.enter_value(Locators.PASSWORD_FIELD, password)

    @allure.step('click to login btn')
    def click_to_login_btn(self):
        self.click(Locators.LOGIN_BTN)

    @allure.step('Open menu')
    def click_to_bm_burger_button(self):
        self.click(Locators.OPEN_MENU)

    @allure.step('Log out account')
    def click_to_logout_sidebar_link(self):
        self.click(Locators.LOGOUT)

    @allure.title('Successful login')
    def check_title(self):
        expected_result = 'Products'
        actual_result = self.is_visible(Locators.TITLE).text
        self.check_equal(expected_result, actual_result)

    @allure.step('Enter wrong username')
    def enter_wrong_username(self, username):
        self.enter_value(Locators.USERNAME_FIELD, username)

    @allure.description('Error message')
    def check_error_message_container(self, error_message):
        actual_result = self.is_visible(Locators.ERROR).text
        self.check_equal(error_message, actual_result)











