"""Forgot password page tests."""
import pytest


class TestForgotPassword:
    """Tests for the forgot password functionality."""

    @pytest.mark.xfail(
        reason="BUG-012: Forgot password always shows success regardless of input"
    )
    def test_unregistered_email_does_not_show_success(self, forgot_password_page):
        """TC-048: Submitting an unregistered email should not claim a reset link was sent."""
        page = forgot_password_page

        page.email.input("absolutely_not_registered@fake.com")
        page.submit_button.click()

        # Should NOT show a success message for a non-existent account
        # (A generic message is acceptable for security, but not a definitive "sent!" success)
        page.message.wait_until_displayed()
        assert not page.message.is_success(), (
            "Should not show success message for unregistered email"
        )
