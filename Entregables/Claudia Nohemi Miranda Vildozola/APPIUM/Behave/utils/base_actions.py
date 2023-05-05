from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException


class BaseActions(object):  # clase padre
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def assert_text(self, *locator, text):
        element_text = self.find_element(*locator).text
        assert element_text == text

    def tap_element(self, *locator):
        action = TouchAction(self.driver)
        action.tap(self.find_element(*locator)).perform()

    def fill_text(self, *locator, text):
        text_field = self.find_element(*locator)
        text_field.send_keys(text)

    def get_text_of_element(self, *locator):
        self.driver.find_element(*locator).text

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def productos_mostrados(self, *locator):
        try:
            self.get_element(*locator)
            return True
        except NoSuchElementException:
            return False