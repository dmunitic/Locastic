from .base_page import BasePage
from .components import BaseElement, Button


class DashboardPage(BasePage):
    URL = "/dashboard.html"

    def __init__(self, page):
        super().__init__(page)

        # Elements
        self.user_name_display = BaseElement(page, "#userName")
        self.logout_button = Button(page, "button.btn-secondary")

    def get_displayed_name(self):
        return self.user_name_display.locator.text_content().strip()
