from .base_element import BaseElement


class Link(BaseElement):
    """Anchor/link element."""

    def click(self):
        self._locator.click()

    def get_text(self):
        return self._locator.text_content().strip()

    def get_href(self):
        return self._locator.get_attribute("href")
