import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


PRODUCT_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
PROMO_URLS = [f"{PRODUCT_URL}?promo=offer{offer}" for offer in range(10)]


def add_product_and_check(page):
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_name_in_basket(product_name)
    page.should_be_product_price_in_basket(product_price)


@pytest.mark.parametrize(
    "link",
    [
        *PROMO_URLS[:7],
        pytest.param(
            PROMO_URLS[7],
            marks=pytest.mark.xfail(
                reason="offer7 success message contains the wrong product name"
            ),
        ),
        *PROMO_URLS[8:],
    ],
)
def test_product_page_promo_offers(browser, link):
    page = ProductPage(browser, link)
    page.open()
    add_product_and_check(page)


@pytest.mark.xfail(reason="A success message appears after adding the product")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, f"{PRODUCT_URL}?promo=offer0")
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_see_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, f"{PRODUCT_URL}?promo=offer0")
    page.open()
    page.should_not_see_success_message()


@pytest.mark.xfail(reason="The success message remains visible beyond the 4-second wait")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, f"{PRODUCT_URL}?promo=offer0")
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_success_message_disappear()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, f"{PRODUCT_URL}?promo=offer0")
    page.open()
    add_product_and_check(page)


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.go_to_basket()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser, user):
    page = ProductPage(browser, PRODUCT_URL)
    page.open()
    add_product_and_check(page)


