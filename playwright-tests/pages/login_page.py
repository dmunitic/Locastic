from .base_page import BasePage
from .components import TextField, Button, Checkbox, Link, Message


class LoginPage(BasePage):
    URL = "/index.html"

    def __init__(self, page):
        super().__init__(page)

        # Text fields
        self.email = TextField(
            page, "#loginEmail", error_locator_str="#loginEmailError"
        )
        self.password = TextField(
            page, "#loginPassword", error_locator_str="#loginPasswordError"
        )

        # Checkbox
        self.remember_me = Checkbox(page, "#rememberMe")

        # Button
        self.login_button = Button(page, "button[type='submit']")

        # Links
        self.forgot_password_link = Link(page, "a[href='forgot-password.html']")
        self.register_link = Link(page, "a[href='register.html']")

        # Messages
        self.message = Message(page, "#loginMessage")

    def login(self, email, password):
        """Fill credentials and click Login."""
        self.email.input(email)
        self.password.input(password)
        self.login_button.click()
