import pytest

from framework import LoginPage


@pytest.fixture(scope='class')
def user_login_fixture(get_driver_ajaxsystems):
    yield LoginPage(get_driver_ajaxsystems)
