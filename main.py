import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

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


def test_connection():
    driver = webdriver.Remote(appium_server_url, capabilities)
    assert driver.current_context == 'NATIVE_APP'

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
