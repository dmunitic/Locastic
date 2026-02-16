# QA Test Application - Playwright Automation Suite

Automated test suite for the [QA Test Web Application](https://qa-test-web-app.vercel.app/) registration flow, built with **Python**, **Playwright**, and **pytest**.

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd playwright-tests

# Create and activate a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

## Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with visible browser (headed mode)
pytest --headed

# Run specific test file
pytest tests/test_registration_happy_path.py

# Run by marker
pytest -m smoke            # Core functionality only
pytest -m mobile           # Mobile viewport tests
pytest -m tablet           # Tablet viewport tests

# Generate HTML report
pytest --html=report.html --self-contained-html

# Run with specific browser
pytest --browser chromium   # default
pytest --browser firefox
pytest --browser webkit
```

## Project Structure

```
playwright-tests/
├── conftest.py                     # Fixtures: viewport contexts, page objects
├── pytest.ini                      # pytest configuration and markers
├── requirements.txt                # Python dependencies
│
├── pages/                          # Page Object Model
│   ├── components/                 # Element-centric component classes
│   │   ├── base_element.py         # BaseElement — shared behavior
│   │   ├── text_field.py           # TextField — input, clear, error messages
│   │   ├── button.py               # Button — click
│   │   ├── checkbox.py             # Checkbox — check, uncheck
│   │   ├── link.py                 # Link — click, get href
│   │   ├── dropdown.py             # Dropdown — select options
│   │   └── message.py              # Message — success/error feedback
│   ├── base_page.py                # BasePage — navigate, get URL/title
│   ├── registration_page.py        # RegistrationPage
│   ├── login_page.py               # LoginPage
│   ├── forgot_password_page.py     # ForgotPasswordPage
│   └── dashboard_page.py           # DashboardPage
│
├── tests/                          # Test files
│   ├── test_navigation.py          # Page navigation tests
│   ├── test_registration_happy_path.py   # Successful registration
│   ├── test_registration_validation.py   # Input validation tests
│   ├── test_registration_responsive.py   # Mobile & tablet viewport tests
│   ├── test_post_registration_flow.py    # Register → login → dashboard
│   └── test_forgot_password.py     # Password reset tests
│
└── test_data/
    └── registration_data.py        # Test data constants and helpers
```

## Architecture: Element-Centric Page Object Model

This project uses an **element-centric POM** where each UI element is a typed object that only exposes actions appropriate to its type:

```python
# Each element knows its own actions — no mismatches possible
registration_page.first_name.input("John")       # TextField.input()
registration_page.terms_checkbox.check()          # Checkbox.check()
registration_page.submit_button.click()           # Button.click()
registration_page.email.get_error_message()       # TextField.get_error_message()
```

This gives us:
- **Type safety**: A `Button` has `.click()`, not `.input()`. A `TextField` has `.input()`, not `.check()`.
- **Readability**: `page.element.action(data)` reads like natural language.
- **IDE support**: Autocomplete shows only valid actions per element type.

## Test Strategy

- Tests assert **correct expected behavior** (what the app *should* do)
- Known bugs are marked with `@pytest.mark.xfail(reason="BUG-XXX: description")`
- xfail tests are expected to fail, documenting the bug. If a bug is fixed, the test auto-alerts (xpass)

## Test Coverage

| File | Tests | Covers |
|------|-------|--------|
| `test_navigation.py` | 2 | TC-001, TC-002 |
| `test_registration_happy_path.py` | 2 | TC-003, TC-004 |
| `test_registration_validation.py` | 18 | TC-005, TC-008, TC-009, TC-010, TC-011, TC-013, TC-017, TC-022, TC-025, TC-027, TC-034, TC-016, TC-020, TC-021a, TC-021b, TC-033, TC-006a, TC-006b |
| `test_registration_responsive.py` | 4 | TC-042, TC-043, TC-044, TC-046 |
| `test_post_registration_flow.py` | 5 | TC-012, TC-035, TC-040, TC-041a, TC-041b |
| `test_forgot_password.py` | 1 | TC-048 |
| **Total** | **32** | |

## Known Bugs Documented via xfail

| Bug ID | Description | Test |
|--------|-------------|------|
| BUG-001 | Weak email regex accepts `user@x` and spaces | `test_email_without_proper_domain_rejected`, `test_email_with_spaces_rejected` |
| BUG-002 | Error messages hidden on mobile | `test_error_messages_visible_on_mobile` |
| BUG-003 | Password min length 4 instead of 8+ | `test_four_char_password_rejected` |
| BUG-004 | Phone accepts alphabetical characters | `test_phone_with_letters_rejected` |
| BUG-006 | Password match always returns true | `test_mismatched_passwords_rejected_client_side`, `test_mismatched_passwords_rejected_end_to_end`, `test_login_uses_password_field_after_mismatch` |
| BUG-007 | Terms checkbox not enforced | `test_terms_unchecked_shows_client_side_error`, `test_terms_unchecked_registration_fails_end_to_end` |
| BUG-008 | ZIP code accepts letters, no upper bound | `test_zip_code_with_letters_rejected`, `test_zip_code_too_long_rejected` |
| BUG-009 | Submit button clipped on mobile | `test_submit_button_fully_visible_on_mobile` |
| BUG-010 | Street Address obscured on tablet | `test_street_address_not_obscured_on_tablet` |
| BUG-011 | Newsletter checkbox obscured on mobile | `test_newsletter_checkbox_visible_on_mobile` |
| BUG-012 | Forgot password always shows success | `test_unregistered_email_does_not_show_success` |
| BUG-014 | No max length validation on text fields | `test_excessively_long_input_rejected` |
| BUG-015 | Name fields accept special symbols | `test_symbols_in_name_fields_rejected` |
| BUG-016 | No input trimming for spaces | `test_email_with_leading_trailing_spaces_rejected` |
