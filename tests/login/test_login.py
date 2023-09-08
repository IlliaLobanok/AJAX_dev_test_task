from framework import LoginPage
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


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


def test_user_login(user_login_fixture):
    current_page = user_login_fixture
    assert current_page.driver.current_context == 'NATIVE_APP'

    button_log_in = current_page.find_element("//*[@text = 'Log In']")
    current_page.tap_element(button_log_in)
    email_box = current_page.find_element("//*[@text = 'email@domain.com']")
    assert email_box is not None

    current_page.tap_element(email_box)
    current_page.enter_text("qa.ajax.app.automation@gmail.com", email_box)

    eye_icon = current_page.find_element("iconPassword", AppiumBy.ID)
    current_page.tap_element(eye_icon)

    # password_box = current_page.find_element("//*[@text = '•••••']")
    # current_page.tap_element(password_box)
    # current_page.enter_text("qa_automation_password", password_box)

    assert True


