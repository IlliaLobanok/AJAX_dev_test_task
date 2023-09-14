import logging
from typing import Union, Optional, List
from selenium.webdriver import ActionChains
from appium.webdriver.webelement import WebElement
from appium.webdriver.common.touch_action import TouchAction


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, value: str, type_by: Optional[str] = "xpath") -> Union[List[WebElement], None]:
        try:
            elements = self.driver.find_elements(by=type_by, value=value)
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.exception(f"While searching for {value}: ")
            return None

        return elements

    def tap_element(self, element: WebElement):
        action = TouchAction(self.driver)
        try:
            action.tap(element).perform()  # tap the button
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.exception(f"While tapping the {element.id}: ")

    def enter_text(self, text: str, element: WebElement):
        try:
            element.send_keys(text)
        except Exception as e:
            try:
                actions = ActionChains(self.driver)
                actions.click(element)
                actions.send_keys(text)
                actions.perform()
            except Exception as e:
                logger = logging.getLogger(__name__)
                logger.exception(f"While sending {text} to {element.id}: ")

    def catch_snackbar(self):
        logger = logging.getLogger(__name__)
        logger.info("Looking for snackbars via catch_snackbars.")
        textview_elements = self.find_elements("android.widget.TextView", "class name")
        if textview_elements is not None:
            for element in textview_elements:
                if element.get_attribute("resource-id") == "com.ajaxsystems:id/snackbar_text":
                    logger.error(f"Snackbar found: {element.text}")
                    return element.text
        logger.info("No snackbars found, exiting function.")
        return None

