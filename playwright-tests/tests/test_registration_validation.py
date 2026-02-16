"""Registration form validation tests."""
import pytest
from test_data.registration_data import get_valid_user


class TestRequiredFields:
    """Required field validation."""

    @pytest.mark.smoke
    def test_empty_form_submission_blocked(self, registration_page):
        """TC-005: Submitting empty form should be blocked by required field validation."""
        registration_page.submit_form()

        # Form should not navigate away — we should still be on register page
        assert "register.html" in registration_page.get_url()

        # No success message should appear
        assert not registration_page.message.is_displayed()


class TestEmailValidation:
    """Email field validation."""

    def test_email_without_at_symbol_rejected(self, registration_page):
        """TC-008: Email without @ symbol should be rejected."""
        user = get_valid_user()
        user["email"] = "notanemail.com"

        registration_page.fill_form(user)
        registration_page.submit_form()

        assert registration_page.email.has_error()
        assert "Invalid email" in registration_page.email.get_error_message()

    def test_email_without_domain_rejected(self, registration_page):
        """TC-009: Email 'user@' (missing domain) should be rejected."""
        user = get_valid_user()
        user["email"] = "user@"

        registration_page.fill_form(user)
        registration_page.submit_form()

        assert registration_page.email.has_error()
        assert "Invalid email" in registration_page.email.get_error_message()

    @pytest.mark.xfail(
        reason="BUG-001: Weak email regex /\\S+@\\S/ accepts 'user@x' as valid"
    )
    def test_email_without_proper_domain_rejected(self, registration_page):
        """TC-010: Email 'user@x' should be rejected (no valid TLD)."""
        user = get_valid_user()
        user["email"] = "user@x"

        registration_page.fill_form(user)
        registration_page.submit_form()

        assert registration_page.email.has_error()

    @pytest.mark.xfail(
        reason="BUG-001: Weak email regex /\\S+@\\S/ accepts spaces in email"
    )
    def test_email_with_spaces_rejected(self, registration_page):
        """TC-011: Email with spaces 'user name@email.com' should be rejected."""
        user = get_valid_user()
        user["email"] = "user name@email.com"

        registration_page.fill_form(user)
        registration_page.submit_form()

        assert registration_page.email.has_error()


class TestNameFieldValidation:
    """Name field character validation."""

    @pytest.mark.xfail(
        reason="BUG-015: No character validation on name fields — symbols like @#$%^& accepted"
    )
    def test_symbols_in_name_fields_rejected(self, registration_page):
        """TC-025: Special symbols (@#$%^&) in name fields should be rejected."""
        user = get_valid_user()
        user["first_name"] = "John@#$"
        user["last_name"] = "Doe%^&"

        registration_page.fill_form(user)
        registration_page.submit_form()

        # Should stay on registration page with no success
        registration_page.message.wait_until_displayed()
        assert not registration_page.message.is_success(), (
            "Registration should not succeed with symbols in name fields"
        )


class TestInputTrimming:
    """Input trimming and whitespace handling."""

    @pytest.mark.xfail(
        reason="BUG-016: No input trimming — leading/trailing spaces in email accepted as-is"
    )
    def test_email_with_leading_trailing_spaces_rejected(self, registration_page):
        """TC-027: Email with leading/trailing spaces should be trimmed or rejected.

        Currently spaces are stored verbatim, so users must type the spaces
        to log in — which is unexpected and error-prone.
        """
        user = get_valid_user()
        user["email"] = f"  {user['email']}  "

        registration_page.fill_form(user)
        registration_page.submit_form()

        registration_page.message.wait_until_displayed()
        assert not registration_page.message.is_success(), (
            "Registration should not succeed with leading/trailing spaces in email"
        )


class TestPhoneValidation:
    """Phone number validation."""

    @pytest.mark.xfail(
        reason="BUG-004: Phone validation only checks length > 0, accepts any characters"
    )
    def test_phone_with_letters_rejected(self, registration_page):
        """TC-013: Alphabetical phone number should be rejected."""
        user = get_valid_user()
        user["phone"] = "abcd-efg-hijk"

        registration_page.fill_form(user)
        registration_page.submit_form()

        assert registration_page.phone.has_error()
        assert "Invalid phone" in registration_page.phone.get_error_message()


class TestPasswordValidation:
    """Password field validation."""

    @pytest.mark.xfail(
        reason="BUG-003: Password minimum is 4 chars instead of industry-standard 8+"
    )
    def test_four_char_password_rejected(self, registration_page):
        """TC-017: Password '1234' should be rejected (too weak)."""
        user = get_valid_user()
        user["password"] = "1234"
        user["confirm_password"] = "1234"

        registration_page.fill_form(user)
        registration_page.submit_form()

        assert registration_page.password.has_error()

    @pytest.mark.xfail(
        reason="BUG-006: validatePasswordMatch() always returns true"
    )
    def test_mismatched_passwords_rejected_client_side(self, registration_page):
        """TC-016: Client-side validation should catch mismatched passwords
        and show an error BEFORE submitting to the server."""
        user = get_valid_user()
        user["password"] = "SecurePass123!"
        user["confirm_password"] = "CompletelyDifferent456!"

        registration_page.fill_form(user)
        registration_page.submit_form()

        # Client-side should show error immediately (no API wait needed)
        assert registration_page.confirm_password.has_error()
        assert "do not match" in registration_page.confirm_password.get_error_message()


class TestZipCodeValidation:
    """ZIP code validation."""

    @pytest.mark.xfail(
        reason="BUG-008: ZIP validation only checks length >= 3, accepts letters"
    )
    def test_zip_code_with_letters_rejected(self, registration_page):
        """TC-020: Alphabetical ZIP code 'ABCDE' should be rejected."""
        user = get_valid_user()
        user["zip_code"] = "ABCDE"

        registration_page.fill_form(user)
        registration_page.submit_form()

        assert registration_page.zip_code.has_error()

    def test_zip_code_too_short_rejected(self, registration_page):
        """TC-021a: ZIP code '12' (2 chars) should be rejected as too short."""
        user = get_valid_user()
        user["zip_code"] = "12"

        registration_page.fill_form(user)
        registration_page.submit_form()

        assert registration_page.zip_code.has_error()
        assert "Invalid ZIP" in registration_page.zip_code.get_error_message()

    @pytest.mark.xfail(
        reason="BUG-008: ZIP validation has no upper bound, only checks length >= 3"
    )
    def test_zip_code_too_long_rejected(self, registration_page):
        """TC-021b: ZIP code '123456789' (9 digits) should be rejected as too long."""
        user = get_valid_user()
        user["zip_code"] = "123456789"

        registration_page.fill_form(user)
        registration_page.submit_form()

        assert registration_page.zip_code.has_error()


class TestTermsValidation:
    """Terms and Conditions checkbox enforcement."""

    @pytest.mark.xfail(
        reason="BUG-007: Terms checkbox validation is commented out in source code"
    )
    def test_terms_unchecked_shows_client_side_error(self, registration_page):
        """TC-006a: Client-side validation should prevent submission without
        accepting Terms and Conditions, showing an error message immediately."""
        user = get_valid_user()
        user["accept_terms"] = False

        registration_page.fill_form(user)
        registration_page.submit_form()

        # Client-side should block submission and show an error (no API wait)
        assert registration_page.message.is_displayed()
        assert registration_page.message.is_error()

    @pytest.mark.xfail(
        reason="BUG-007: Neither client nor server enforces Terms acceptance"
    )
    def test_terms_unchecked_registration_fails_end_to_end(self, registration_page):
        """TC-006b: Even if client-side is bypassed, registration should not
        succeed without Terms acceptance (server-side enforcement)."""
        user = get_valid_user()
        user["accept_terms"] = False

        registration_page.fill_form(user)
        registration_page.submit_form()

        # Wait for the API response to arrive
        registration_page.message.wait_until_displayed()

        # Registration should NOT succeed without terms
        assert not registration_page.message.is_success(), (
            "Registration should not succeed without accepting Terms and Conditions"
        )


class TestMaxLengthValidation:
    """Input length boundary validation."""

    @pytest.mark.xfail(
        reason="BUG-014: No maxlength attribute or length validation — 300+ char strings "
               "accepted and break the dashboard display"
    )
    def test_excessively_long_input_rejected(self, registration_page):
        """TC-022: 300+ character strings in text fields should be rejected or truncated."""
        long_string = "A" * 300
        user = get_valid_user()
        user["first_name"] = long_string
        user["last_name"] = long_string
        user["address"] = long_string
        user["city"] = long_string

        registration_page.fill_form(user)
        registration_page.submit_form()

        registration_page.message.wait_until_displayed()
        assert not registration_page.message.is_success(), (
            "Registration should not succeed with 300+ character input fields"
        )


class TestSecurityInputHandling:
    """Basic security input handling tests."""

    def test_sql_injection_in_fields_does_not_cause_error(self, registration_page):
        """TC-034: SQL injection strings should not cause server errors or crashes."""
        user = get_valid_user()
        user["first_name"] = "'; DROP TABLE users; --"
        user["last_name"] = "' OR '1'='1"
        user["address"] = "1; DELETE FROM accounts"
        user["city"] = "' UNION SELECT * FROM users --"

        registration_page.fill_form(user)
        registration_page.submit_form()

        registration_page.message.wait_until_displayed()

        # The app should handle this gracefully — either succeed (input escaped)
        # or show a clean validation error. No SQL error or crash.
        assert registration_page.message.is_displayed(), (
            "App should respond with a message, not crash"
        )
        message_text = registration_page.message.get_text()
        assert "error" not in message_text.lower() or "sql" not in message_text.lower(), (
            f"Possible SQL error exposed to user: {message_text}"
        )


class TestFormDataPersistence:
    """Form data preservation after validation errors."""

    def test_field_values_preserved_after_validation_error(self, registration_page):
        """TC-033: Previously entered data should remain in fields after a validation error."""
        user = get_valid_user()
        user["email"] = "notanemail"  # Trigger validation error

        registration_page.fill_form(user)
        registration_page.submit_form()

        # Validation should fail
        assert registration_page.email.has_error()

        # All other field values should be preserved
        assert registration_page.first_name.get_value() == user["first_name"]
        assert registration_page.last_name.get_value() == user["last_name"]
        assert registration_page.email.get_value() == user["email"]
        assert registration_page.phone.get_value() == user["phone"]
        assert registration_page.address.get_value() == user["address"]
        assert registration_page.city.get_value() == user["city"]
        assert registration_page.zip_code.get_value() == user["zip_code"]
