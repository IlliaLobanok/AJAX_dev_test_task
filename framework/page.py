import logging
from typing import Union, Optional, List
from selenium.webdriver import ActionChains
from appium.webdriver.webelement import WebElement
from appium.webdriver.common.touch_action import TouchAction


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, value: str, by_type: Optional[str] = "class name", attr_value: Optional[str] = None,
                      attribute: Optional[str] = "resource-id") -> Union[List[WebElement], WebElement, None]:
        logger = logging.getLogger(__name__)
        logger.info(f"Started looking for {by_type} with {value}.")

        try:
            elements = self.driver.find_elements(by=by_type, value=value)
        except Exception as e:
            logger.exception(f"While searching for {by_type} with {value}: ")
            return None

        if attr_value is not None:
            logger.debug(f"Looking for {value} with {attribute} = {attr_value}.")
            found_element = None
            for element in elements:
                if element.get_attribute(attribute) == attr_value:
                    found_element = element

            if found_element is None:
                logger.error(f"{by_type} of {value} with {attribute} of {attr_value} not found.")
                return None
            else:
                logger.info(f"{by_type} of {value} with {attribute} of {attr_value} found successfully.")
                return found_element
        else:
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

        snackbar = self.find_elements(value="android.widget.TextView", attr_value="com.ajaxsystems:id/snackbar_text")
        if snackbar is not None:
            logger.error(f"Snackbar found: {snackbar.text}")
            return snackbar.text
        logger.info("No snackbars found.")
        return None

