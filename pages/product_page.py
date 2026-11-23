from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip()

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.strip()

    def should_be_product_name_in_basket(self, expected_name):
        actual_name = self.browser.find_element(
            *ProductPageLocators.BASKET_PRODUCT_NAME
        ).text.strip()
        assert actual_name == expected_name, (
            f"Basket product name is {actual_name!r}; expected {expected_name!r}"
        )

    def should_be_product_price_in_basket(self, expected_price):
        actual_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRODUCT_PRICE
        ).text.strip()
        assert actual_price == expected_price, (
            f"Basket price is {actual_price!r}; expected {expected_price!r}"
        )

    def should_not_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Success message is present"
        )

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Success message did not disappear"
        )
