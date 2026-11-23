from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        message = self.browser.find_element(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE
        ).text.strip()
        assert "basket is empty" in message.lower(), (
            f"Expected an empty basket message, got {message!r}"
        )
