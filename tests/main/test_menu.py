import pytest
import logging


class TestBurgerMenu:
    def test_is_main(self, main_page_fixture):
        logger = logging.getLogger(__name__)
        logger.info("Started test_is_main.")

        current_page = main_page_fixture
        try:
            assert current_page.driver.current_context == "NATIVE_APP"
        except AssertionError as error:
            logger.error(f"Did not make it to native app: {error}")

        assert current_page.is_main()

    def test_burger_menu(self, main_page_fixture):
        logger = logging.getLogger(__name__)
        logger.info("Started test_burger_menu.")

        current_page = main_page_fixture
        try:
            assert current_page.driver.current_context == "NATIVE_APP"
        except AssertionError as error:
            logger.error(f"Did not make it to native app: {error}")

        assert current_page.open_burger_menu()

    def test_settings(self, main_page_fixture):
        logger = logging.getLogger(__name__)
        logger.info("Started test_settings.")

        current_page = main_page_fixture
        try:
            assert current_page.driver.current_context == "NATIVE_APP"
        except AssertionError as error:
            logger.error(f"Did not make it to native app: {error}")

        assert current_page.open_settings()


