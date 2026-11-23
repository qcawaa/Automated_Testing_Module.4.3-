import math

from selenium.common.exceptions import (
    NoAlertPresentException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, *locator, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, *locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, *locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), (
            "Login link is not presented"
        )

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), (
            "User icon is not presented; user is not authorized"
        )

    def go_to_basket(self):
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

    def solve_quiz_and_get_code(self):
        try:
            alert = self.browser.switch_to.alert
        except NoAlertPresentException:
            print("No quiz alert presented")
            return

        number = alert.text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(float(number)))))
        alert.send_keys(answer)
        alert.accept()

        try:
            alert = self.browser.switch_to.alert
            code = alert.text
            print(f"Your code: {code}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

