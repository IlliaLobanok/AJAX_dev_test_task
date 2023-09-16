import pytest

from framework import LoginPage, MainPage


@pytest.fixture(scope='class')
def main_page_fixture(get_driver_ajaxsystems):
    page = LoginPage(get_driver_ajaxsystems)
    if page.log_in() is None:
        return MainPage(page.driver)
