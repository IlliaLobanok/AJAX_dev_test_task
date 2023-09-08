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

    button_log_in = current_page.find_elements("//*[@text = 'Log In']")
    current_page.tap_element(button_log_in[0])
    credents_boxes = current_page.find_elements('android.widget.EditText', AppiumBy.CLASS_NAME)
    assert credents_boxes is not None

    current_page.tap_element(credents_boxes[0])
    current_page.enter_text(current_page.email, credents_boxes[0])

    current_page.tap_element(credents_boxes[1])
    current_page.enter_text(current_page.password, credents_boxes[1])

    view_elements = current_page.find_elements("android.view.View", AppiumBy.CLASS_NAME)
    assert view_elements is not None
    eye_icon = None
    for element in view_elements:
        if element.get_attribute("resource-id") == "iconPassword":
            eye_icon = element
    if eye_icon is not None:
        current_page.tap_element(eye_icon)
    else:
        pytest.skip("Unable to find eye icon element")

    assert credents_boxes[0].text == current_page.email
    assert credents_boxes[1].text == current_page.password


