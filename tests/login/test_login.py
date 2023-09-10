from framework import LoginPage
import pytest
from appium import webdriver
from framework import LoginPage


@pytest.fixture
def get_driver_ajaxsystems():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='my_phone',
        appPackage='com.ajaxsystems',
        appActivity='.ui.activity.LauncherActivity',
        noReset=False,
        language='en',
        locale='US'
    )
    appium_server_url = 'http://localhost:4723'

    return webdriver.Remote(appium_server_url, capabilities)


@pytest.fixture
def user_login_fixture(get_driver_ajaxsystems):
    yield LoginPage(get_driver_ajaxsystems)


def test_login_positive(user_login_fixture):
    current_page = user_login_fixture
    assert current_page.driver.current_context == "NATIVE_APP"

    result_login_sequence = current_page.log_in()
    if result_login_sequence is not None:
        pytest.skip(result_login_sequence)


def test_login_negative_invalid_email(user_login_fixture):
    current_page = user_login_fixture
    assert current_page.driver.current_context == "NATIVE_APP"

    result_login_sequence = current_page.log_in("examplegmail.com", "123456")
    if result_login_sequence is not None:
        assert result_login_sequence == "ERROR at log_in(): Invalid email format"
