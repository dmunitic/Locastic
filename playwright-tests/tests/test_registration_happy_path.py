"""Happy path registration tests."""
import pytest
from test_data.registration_data import get_valid_user


class TestRegistrationHappyPath:
    """Successful registration scenarios."""

    @pytest.mark.smoke
    def test_successful_registration_with_valid_data(self, registration_page):
        """TC-003: Register with all valid fields, terms accepted."""
        user = get_valid_user()

        registration_page.fill_form(user)
        registration_page.submit_form()

        registration_page.message.wait_until_displayed()
        assert registration_page.message.is_success()
        assert "Registration successful" in registration_page.message.get_text()

    @pytest.mark.smoke
    def test_registration_without_newsletter(self, registration_page):
        """TC-004: Registration succeeds without newsletter subscription."""
        user = get_valid_user()
        user["subscribe_newsletter"] = False

        registration_page.fill_form(user)
        registration_page.submit_form()

        registration_page.message.wait_until_displayed()
        assert registration_page.message.is_success()
