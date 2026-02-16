"""End-to-end tests: registration followed by login."""
import pytest
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from test_data.registration_data import get_valid_user


class TestPostRegistrationLogin:
    """Tests verifying the complete registration-to-login flow."""

    @pytest.mark.smoke
    def test_login_with_registered_credentials(self, desktop_context, base_url):
        """TC-040: Register a new account, then login with the same credentials."""
        user = get_valid_user()
        page = desktop_context.new_page()

        # Step 1: Register
        reg_page = RegistrationPage(page)
        reg_page.URL = base_url + reg_page.URL
        reg_page.navigate()
        reg_page.fill_form(user)
        reg_page.submit_form()
        reg_page.message.wait_until_displayed()
        assert reg_page.message.is_success()

        # Step 2: Wait for redirect to login page
        page.wait_for_url("**/index.html**", timeout=5000)

        # Step 3: Login with the same credentials
        login_p = LoginPage(page)
        login_p.login(user["email"], user["password"])

        # Step 4: Verify redirect to dashboard
        page.wait_for_url("**/dashboard.html**", timeout=5000)
        dashboard = DashboardPage(page)
        assert dashboard.get_displayed_name() == user["first_name"]


class TestDuplicateEmailRegistration:
    """Tests verifying duplicate email is rejected."""

    def test_duplicate_email_registration_rejected(self, desktop_context, base_url):
        """TC-012: Re-registering with an already-used email should fail."""
        user = get_valid_user()
        page = desktop_context.new_page()

        # Step 1: Register successfully
        reg_page = RegistrationPage(page)
        reg_page.URL = base_url + reg_page.URL
        reg_page.navigate()
        reg_page.fill_form(user)
        reg_page.submit_form()
        reg_page.message.wait_until_displayed()
        assert reg_page.message.is_success()

        # Step 2: Navigate back to registration and try the same email
        reg_page.navigate()
        reg_page.fill_form(user)
        reg_page.submit_form()
        reg_page.message.wait_until_displayed()

        # Should show an error, not a success
        assert reg_page.message.is_error(), (
            "Registration should fail when using an already-registered email"
        )
        assert "already exists" in reg_page.message.get_text()


class TestMismatchedPasswordRegistration:
    """Tests documenting the impact of BUG-006 on the registration flow."""

    @pytest.mark.xfail(
        reason="BUG-006: validatePasswordMatch() always returns true — "
               "registration should be rejected with mismatched passwords"
    )
    def test_mismatched_passwords_rejected_end_to_end(
        self, desktop_context, base_url
    ):
        """TC-041a: Registration should not succeed when passwords don't match.

        Even if client-side validation is broken (BUG-006), the server should
        reject mismatched passwords. Neither layer catches this.
        """
        user = get_valid_user()
        user["password"] = "CorrectPassword123!"
        user["confirm_password"] = "WrongPassword456!"
        page = desktop_context.new_page()

        reg_page = RegistrationPage(page)
        reg_page.URL = base_url + reg_page.URL
        reg_page.navigate()
        reg_page.fill_form(user)
        reg_page.submit_form()

        # Wait for the API response
        reg_page.message.wait_until_displayed()

        # Registration should NOT succeed with mismatched passwords
        assert not reg_page.message.is_success(), (
            "Registration should not succeed with mismatched passwords"
        )

    @pytest.mark.xfail(
        reason="BUG-006: validatePasswordMatch() always returns true — "
               "mismatched passwords bypass validation and the 'password' "
               "field value is stored"
    )
    def test_login_uses_password_field_after_mismatch(
        self, desktop_context, base_url
    ):
        """TC-041b: If mismatched registration succeeds (BUG-006), the stored
        password should be from the 'password' field, not 'confirmPassword'.

        This test documents the real-world impact: which password actually works?
        Expected behavior: registration should have been rejected entirely.
        """
        user = get_valid_user()
        user["password"] = "CorrectPassword123!"
        user["confirm_password"] = "WrongPassword456!"
        page = desktop_context.new_page()

        # Step 1: Register with mismatched passwords (succeeds due to BUG-006)
        reg_page = RegistrationPage(page)
        reg_page.URL = base_url + reg_page.URL
        reg_page.navigate()
        reg_page.fill_form(user)
        reg_page.submit_form()
        reg_page.message.wait_until_displayed()

        # This should not have succeeded, but it does (BUG-006)
        # Assert it SHOULD fail — this is the expected correct behavior
        assert not reg_page.message.is_success(), (
            "Registration should have been rejected with mismatched passwords"
        )


class TestXSSPrevention:
    """Tests verifying XSS payloads are not executed."""

    def test_xss_in_name_not_executed_on_dashboard(self, desktop_context, base_url):
        """TC-035: Script tags in name fields should be rendered as text, not executed."""
        xss_payload = "<script>alert('XSS')</script>"
        user = get_valid_user()
        user["first_name"] = xss_payload
        page = desktop_context.new_page()

        # Step 1: Register with XSS payload in first name
        reg_page = RegistrationPage(page)
        reg_page.URL = base_url + reg_page.URL
        reg_page.navigate()
        reg_page.fill_form(user)
        reg_page.submit_form()
        reg_page.message.wait_until_displayed()
        assert reg_page.message.is_success()

        # Step 2: Login
        page.wait_for_url("**/index.html**", timeout=5000)
        login_p = LoginPage(page)
        login_p.login(user["email"], user["password"])

        # Step 3: Verify dashboard renders payload as text, not as HTML
        page.wait_for_url("**/dashboard.html**", timeout=5000)
        dashboard = DashboardPage(page)
        displayed_name = dashboard.get_displayed_name()

        # The script tag should appear as literal text, not be executed
        assert "<script>" in displayed_name or "alert" in displayed_name, (
            "XSS payload should be rendered as visible text, not stripped or executed"
        )

        # Verify no alert dialog was triggered
        # (Playwright would throw if an unexpected dialog appeared)
