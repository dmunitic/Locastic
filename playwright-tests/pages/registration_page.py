from .base_page import BasePage
from .components import TextField, Button, Checkbox, Link, Message


class RegistrationPage(BasePage):
    URL = "/register.html"

    def __init__(self, page):
        super().__init__(page)

        # Text fields
        self.first_name = TextField(page, "#firstName")
        self.last_name = TextField(page, "#lastName")
        self.email = TextField(page, "#email", error_locator_str="#emailError")
        self.phone = TextField(page, "#phone", error_locator_str="#phoneError")
        self.address = TextField(page, "#address")
        self.city = TextField(page, "#city")
        self.zip_code = TextField(page, "#zipCode", error_locator_str="#zipError")
        self.password = TextField(
            page, "#password", error_locator_str="#passwordError"
        )
        self.confirm_password = TextField(
            page, "#confirmPassword", error_locator_str="#confirmPasswordError"
        )

        # Checkboxes
        self.terms_checkbox = Checkbox(page, "#terms")
        self.newsletter_checkbox = Checkbox(page, "#newsletter")

        # Button
        self.submit_button = Button(page, "button[type='submit']")

        # Links
        self.login_link = Link(page, "a[href='index.html']")

        # Messages
        self.message = Message(page, "#registerMessage")

        # Overlay elements (for responsive testing)
        self.address_overlay = page.locator(
            ".tablet-hidden .overlay-image-tablet"
        )
        self.newsletter_overlay = page.locator(
            ".mobile-hidden-checkbox .overlay-image-small"
        )

    def fill_form(self, data):
        """Fill the entire registration form from a dictionary."""
        self.first_name.input(data.get("first_name", ""))
        self.last_name.input(data.get("last_name", ""))
        self.email.input(data.get("email", ""))
        self.phone.input(data.get("phone", ""))
        self.address.input(data.get("address", ""))
        self.city.input(data.get("city", ""))
        self.zip_code.input(data.get("zip_code", ""))
        self.password.input(data.get("password", ""))
        self.confirm_password.input(data.get("confirm_password", ""))
        if data.get("accept_terms", False):
            self.terms_checkbox.check()
        if data.get("subscribe_newsletter", False):
            self.newsletter_checkbox.check()

    def submit_form(self):
        """Click the Create Account button."""
        self.submit_button.click()
