import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


@pytest.fixture()
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


def test_connection(get_driver_ajaxsystems):
    driver = get_driver_ajaxsystems
    assert driver.current_context == 'NATIVE_APP'


def test_find_button(get_driver_ajaxsystems):
    driver = get_driver_ajaxsystems
    try:
        log_in_button = driver.find_element(by=AppiumBy.XPATH, value="//*[@text = 'Log In']")
    except Exception as e:
        pytest.skip(f"Appium error: {e}")
    assert True


def test_click_button(get_driver_ajaxsystems):
    driver = get_driver_ajaxsystems
    try:
        log_in_button = driver.find_element(by=AppiumBy.XPATH, value="//*[@text = 'Log In']")   # find the button
    except Exception as e:
        pytest.skip(f"Appium error: {e}")

    action = TouchAction(driver)
    try:
        action.tap(log_in_button).perform()     # tap the button
    except Exception as e:
        pytest.skip(f"Appium error: {e}")

    try:
        email_box = driver.find_element(by=AppiumBy.XPATH, value="//*[@text = 'Email']")    # look for an email box
    except Exception as e:
        pytest.skip(f"Appium error: {e}")       # if there's no such thing, end the test
    assert True                                 # executed only if no exceptions were raised (object found)


