from typing import Union, Optional, List
# from selenium.webdriver import ActionChains
from appium.webdriver.webelement import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, value: str, type_by: Optional[str] = AppiumBy.XPATH) -> Union[List[WebElement], None]:
        try:
            elements = self.driver.find_elements(by=type_by, value=value)
        except Exception as e:
            print(f"Appium error: {e}")
            return None

        return elements

    def tap_element(self, element: WebElement):
        action = TouchAction(self.driver)
        try:
            action.tap(element).perform()  # tap the button
        except Exception as e:
            print(f"Appium error: {e}")

    def enter_text(self, text: str, element: WebElement):
        try:
            element.send_keys(text)
        except Exception as e:
            print(f"Appium error: {e}")

    # def enter_text(self, text: str, element: WebElement):
    #     try:
    #         element.send_keys(text)
    #     except Exception as e:
    #         try:
    #             actions = ActionChains(self.driver)
    #             actions.click(element)
    #             actions.send_keys(text)
    #             actions.perform()
    #         except Exception as e:
    #             print(f"Appium error: {e}")
