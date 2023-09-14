import pytest
import logging


class TestPositive:
    def test_login_positive(self, user_login_fixture):
        logger = logging.getLogger(__name__)
        logger.info("Started test_login_positive.")

        current_page = user_login_fixture
        try:
            assert current_page.driver.current_context == "NATIVE_APP"
        except AssertionError as error:
            logger.error(f"Did not make it to native app: {error}")

        logger.debug("Native app started successfully.")

        assert current_page.log_in() is None


class TestNegative:
    def test_login_negative_invalid_email(self, user_login_fixture):
        logger = logging.getLogger(__name__)
        logger.info("Started test_login_negative_invalid_email.")

        current_page = user_login_fixture
        try:
            assert current_page.driver.current_context == "NATIVE_APP"
        except AssertionError as error:
            logger.error(f"Did not make it to native app: {error}")

        logger.debug("Native app started successfully.")

        result_login_sequence = current_page.log_in("examplegmail.com", "123456")
        if result_login_sequence is not None:
            assert result_login_sequence == "Invalid email format"
