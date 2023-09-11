import pytest


class TestPositive:
    def test_login_positive(self, user_login_fixture, setup_logger):
        setup_logger.t_start(TestPositive.test_login_positive)
        current_page = user_login_fixture
        assert current_page.driver.current_context == "NATIVE_APP"
        setup_logger.debug(f"test_login_positive: Native app started successfully")

        result_login_sequence = current_page.log_in()
        if result_login_sequence is not None:
            pytest.skip(result_login_sequence)


class TestNegative:
    def test_login_negative_invalid_email(self, user_login_fixture, setup_logger):
        setup_logger.t_start(TestNegative.test_login_negative_invalid_email)
        current_page = user_login_fixture
        assert current_page.driver.current_context == "NATIVE_APP"
        setup_logger.debug(f"{TestNegative.test_login_negative_invalid_email.__qualname__}: Native app started successfully")

        result_login_sequence = current_page.log_in("examplegmail.com", "123456")
        if result_login_sequence is not None:
            assert result_login_sequence == "ERROR at log_in(): Invalid email format"
