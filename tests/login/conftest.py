import pytest

from framework.login_page import LoginPage


@pytest.fixture(scope='session')
def user_login_fixture(driver):
    yield LoginPage(driver)
