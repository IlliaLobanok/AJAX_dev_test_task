import logging
from typing import Literal

from .page import Page


class MainPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def is_main(self):
        logger = logging.getLogger(__name__)
        logger.info("Started is_main check function.")

        add_hub_button = self.find_elements(value="android.view.ViewGroup", attr_value="com.ajaxsystems:id/hubAdd")
        menu_button = self.find_elements(value="android.widget.ImageView", attr_value="com.ajaxsystems:id/menuDrawer")

        if add_hub_button is not None and menu_button is not None:
            logger.debug("Add hub & burger menu buttons found successfully.")
            return True
        else:
            logger.error("No add hub or burger menu buttons found on current page. Make sure log in process is OK.")
            return False

    def open_burger_menu(self):
        logger = logging.getLogger(__name__)
        logger.info("Started open_burger_menu sequence.")

        if not self.is_main():
            logger.error("Current page is not main. open_burger_menu stopped.")
            return False

        if self.is_menu_opened():
            logger.debug("Menu is already opened.")
            return True

        menu_button = self.find_elements(value="android.widget.ImageView", attr_value="com.ajaxsystems:id/menuDrawer")
        if menu_button is None:
            logger.error("No menu buttons found.")
            return False

        if self.tap_element(menu_button):
            logger.debug("Burger menu opened successfully.")
            return True
        else:
            logger.error("Burger menu opening failed on button tapping stage.")
            return False

    def is_menu_opened(self):
        logger = logging.getLogger(__name__)
        logger.info("Started is_menu_opened check function.")

        settings_button = self.find_elements(value="android.view.View", attr_value="com.ajaxsystems:id/settings")
        help_button = self.find_elements(value="android.view.View", attr_value="com.ajaxsystems:id/help")
        if settings_button is None and help_button is None:
            logger.debug("No settings & help buttons found. Menu is not opened.")
            return False
        else:
            logger.debug("Settings & help buttons found.")
            return True

    def open_menu_item(self, item=Literal["settings", "help", "logs", "camera"]):
        logger = logging.getLogger(__name__)
        logger.info(f"Started open_menu_item sequence for {item}.")

        if not self.open_burger_menu():
            logger.error("Failed to open burger_menu.")
            return False

        item_button = self.find_elements(value="android.view.View", attr_value=f"com.ajaxsystems:id/{item}")
        if item_button is None:
            logger.error(f"No {item} button found.")
            return False

        if self.tap_element(item_button):
            return True
        else:
            return False

    def log_out(self):
        pass
