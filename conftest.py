import uuid

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose the browser interface language",
    )


@pytest.fixture
def browser(request):
    language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": language}
    )
    options.add_argument(f"--lang={language}")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def user(browser):
    from pages.login_page import LoginPage

    email = f"selenium-test-{uuid.uuid4().hex}@example.com"
    password = "CourseTestPassword123!"
    login_page = LoginPage(
        browser,
        "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/",
    )
    login_page.open()
    login_page.register_new_user(email, password)
    return {"email": email, "password": password}
