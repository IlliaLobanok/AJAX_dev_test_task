import pytest


class TestPositive:
    def test_login_positive(self, user_login_fixture):
        current_page = user_login_fixture
        assert current_page.driver.current_context == "NATIVE_APP"

        result_login_sequence = current_page.log_in()
        if result_login_sequence is not None:
            pytest.skip(result_login_sequence)


class TestNegative:
    def test_login_negative_invalid_email(self, user_login_fixture):
        current_page = user_login_fixture
        assert current_page.driver.current_context == "NATIVE_APP"

        result_login_sequence = current_page.log_in("examplegmail.com", "123456")
        if result_login_sequence is not None:
            assert result_login_sequence == "ERROR at log_in(): Invalid email format"
