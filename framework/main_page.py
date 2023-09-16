import logging

from .page import Page


class MainPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def is_main(self):
        logger = logging.getLogger(__name__)
        logger.info("Started is_main check function.")

        add_hub_button = self.find_elements(value="android.view.ViewGroup", attr_value="com.ajaxsystems:id/hubAdd")
        if add_hub_button is not None:
            logger.debug("Add hub button found successfully.")
            return True
        else:
            logger.error("No add hub buttons found on current page. Make sure log in process is OK.")
            return False

    def open_burger_menu(self):
        logger = logging.getLogger(__name__)
        logger.info("Started open_burger_menu sequence.")

        if not self.is_main():
            logger.error("Current page is not main. open_burger_menu stopped.")
            return False

        if self.is_menu_opened():
            return True

        menu_button = self.find_elements(value="android.widget.ImageView", attr_value="com.ajaxsystems:id/menuDrawer")
        if menu_button is None:
            logger.error("No menu buttons found.")
            return False

        if self.tap_element(menu_button):
            return True
        else:
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

    def open_settings(self):
        logger = logging.getLogger(__name__)
        logger.info("Started open_settings sequence.")

        if not self.open_burger_menu():
            logger.error("Failed to open burger_menu.")
            return False

        settings_button = self.find_elements(value="android.view.View", attr_value="com.ajaxsystems:id/settings")
        if settings_button is None:
            logger.error("No settings button found.")
            return False

        if self.tap_element(settings_button):
            return True
        else:
            return False

    def log_out(self):
        pass


