from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BaseObject:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_present(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    def is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click(self, locator):
        self.is_clickable(locator).click()

    def enter_value(self, locator, value):
        self.is_visible(locator).send_keys(value)

    def check_equal(self, actual_result, expected_result):
        assert actual_result == expected_result, 'failed'

    def get_text(self, locator):
        return self.is_visible(locator).text




