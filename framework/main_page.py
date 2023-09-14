import logging

from .page import Page


class MainPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def is_main(self):
        logger = logging.getLogger(__name__)
        logger.info("Started is_main check function.")

        view_groups = self.find_elements("android.view.ViewGroup", "class name")
        add_hub_button = None
        if view_groups is not None:
            for element in view_groups:
                if element.get_attribute("resource-id") == "com.ajaxsystems:id/hubAdd":
                    add_hub_button = element
        else:
            logger.error("No view_groups found on current page. Make sure log in process is OK.")
            return False
        
        if add_hub_button is not None:
            logger.debug("Add hub button found successfully.")
            return True
        else:
            logger.error("No add hub buttons found among view_groups on current page. Make sure log in process is OK.")
            return False

    def open_burger_menu(self):
        logger = logging.getLogger(__name__)
        logger.info("Started open_burger_menu sequence.")

        if not self.is_main():
            logger.error("Current page is not main. open_burger_menu stopped.")
            return False

        image_views = self.find_elements("android.widget.ImageView", "class name")
        menu_button = None
        if image_views is not None:
            for element in image_views:
                if element.get_attribute("resource-id") == "com.ajaxsystems:id/menuDrawer":
                    menu_button = element
        else:
            logger.error("No image_views found.")
            return False

        if menu_button is None:
            logger.error("No menu buttons found among image_views.")
            return False

        self.tap_element(menu_button)

        return None

    def log_out(self):
        pass


