import pytest
import logging


class TestBurgerMenu:
    @pytest.fixture(scope='function', autouse=True)
    def return_to_main(self, main_page_fixture):
        logger = logging.getLogger(__name__)
        logger.info("Started return_to_main sequence.")

        current_page = main_page_fixture
        try:
            assert current_page.driver.current_context == "NATIVE_APP"
        except AssertionError as error:
            logger.error(f"Did not make it to native app: {error}")

        if not current_page.is_main():
            while True:
                logger.debug("Swiping back.")
                current_page.driver.press_keycode(4)
                if current_page.is_main():
                    logger.debug("Main page successfully opened, fixture sequence finished.")
                    break

    def test_burger_menu(self, main_page_fixture):
        logger = logging.getLogger(__name__)
        logger.info("Started test_burger_menu.")

        current_page = main_page_fixture

        assert current_page.open_burger_menu()

    def test_settings(self, main_page_fixture):
        logger = logging.getLogger(__name__)
        logger.info("Started test_settings.")

        current_page = main_page_fixture

        assert current_page.open_menu_item("settings")

    def test_help(self, main_page_fixture):
        logger = logging.getLogger(__name__)
        logger.info("Started test_help.")

        current_page = main_page_fixture

        assert current_page.open_menu_item("help")

    def test_report(self, main_page_fixture):
        logger = logging.getLogger(__name__)
        logger.info("Started test_report.")

        current_page = main_page_fixture

        assert current_page.open_menu_item("logs")

    def test_surveillance(self, main_page_fixture):
        logger = logging.getLogger(__name__)
        logger.info("Started test_surveillance.")

        current_page = main_page_fixture

        assert current_page.open_menu_item("camera")
