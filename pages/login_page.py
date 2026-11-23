from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        assert "login" in self.browser.current_url.lower(), (
            f"Unexpected login URL: {self.browser.current_url}"
        )
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), (
            "Login form is not presented"
        )
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), (
            "Registration form is not presented"
        )

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT).click()
        self.should_be_authorized_user()
