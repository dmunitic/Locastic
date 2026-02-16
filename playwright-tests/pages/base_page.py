class BasePage:
    """Base class for all page objects."""

    URL = ""

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)
        return self

    def get_title(self):
        return self.page.title()

    def get_url(self):
        return self.page.url

    def get_heading(self):
        return self.page.locator("h1").text_content().strip()
