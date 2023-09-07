import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


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
    button = driver.find_element(by=AppiumBy.XPATH, value="//*[@text = 'Log In']")
    assert True

# class TestAppium(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver = webdriver.Remote(appium_server_url, capabilities)
#
#     def tearDown(self) -> None:
#         if self.driver:
#             self.driver.quit()
#
#     def test_find_wifi(self) -> None:
#         el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Wi-Fi"]')
#         el.click()
