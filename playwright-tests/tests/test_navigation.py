"""Navigation tests between application pages."""
import pytest


class TestNavigation:
    """TC-001, TC-002: Navigation between login and registration pages."""

    @pytest.mark.smoke
    def test_navigate_to_registration_from_login(self, login_page):
        """TC-001: Login page 'Create New Account' link navigates to registration."""
        login_page.register_link.click()

        assert "register.html" in login_page.page.url
        assert login_page.page.locator("h1").text_content().strip() == "Create Account"

    @pytest.mark.smoke
    def test_navigate_to_login_from_registration(self, registration_page):
        """TC-002: Registration page 'Already have an account?' link navigates to login."""
        registration_page.login_link.click()

        assert "index.html" in registration_page.page.url
        assert registration_page.page.locator("h1").text_content().strip() == "Welcome Back"
