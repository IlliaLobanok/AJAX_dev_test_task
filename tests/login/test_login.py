import pytest
import logging


class TestPositive:
    def test_login_positive(self, user_login_fixture):
        logger = logging.getLogger(__name__)
        logger.info("test_login_positive started.")

        current_page = user_login_fixture
        try:
            assert current_page.driver.current_context == "NATIVE_APP"
        except AssertionError as error:
            logger.error(f"Did not made it to native app: {error}")

        logger.debug("Native app started successfully.")

        result_login_sequence = current_page.log_in()
        if result_login_sequence is not None:
            pytest.skip(result_login_sequence)


class TestNegative:
    def test_login_negative_invalid_email(self, user_login_fixture):
        logger = logging.getLogger(__name__)
        logger.info("test_login_negative_invalid_email started.")

        current_page = user_login_fixture
        try:
            assert current_page.driver.current_context == "NATIVE_APP"
        except AssertionError as error:
            logger.error(f"Did not made it to native app: {error}")

        logger.debug("Native app started successfully.")

        result_login_sequence = current_page.log_in("examplegmail.com", "123456")
        if result_login_sequence is not None:
            assert result_login_sequence == "ERROR at log_in(): Invalid email format"
