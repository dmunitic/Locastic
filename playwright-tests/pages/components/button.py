from .base_element import BaseElement


class Button(BaseElement):
    """Clickable button element."""

    def click(self):
        self._locator.click()

    def get_text(self):
        return self._locator.text_content().strip()
