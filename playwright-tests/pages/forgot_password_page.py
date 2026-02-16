from .base_page import BasePage
from .components import TextField, Button, Dropdown, Link, Message


class ForgotPasswordPage(BasePage):
    URL = "/forgot-password.html"

    def __init__(self, page):
        super().__init__(page)

        # Text fields
        self.email = TextField(
            page, "#resetEmail", error_locator_str="#resetEmailError"
        )
        self.security_answer = TextField(page, "#securityAnswer")

        # Dropdown
        self.security_question = Dropdown(page, "#securityQuestion")

        # Button
        self.submit_button = Button(page, "button[type='submit']")

        # Links
        self.login_link = Link(page, "a[href='index.html']")
        self.register_link = Link(page, "a[href='register.html']")

        # Messages
        self.message = Message(page, "#forgotPasswordMessage")
