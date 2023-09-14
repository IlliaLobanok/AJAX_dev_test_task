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

        menu_button = self.find_elements(value="android.widget.ImageView", attr_value="com.ajaxsystems:id/menuDrawer")
        if menu_button is None:
            logger.error("No menu buttons found.")
            return False

        self.tap_element(menu_button)

        return None

    def log_out(self):
        pass


