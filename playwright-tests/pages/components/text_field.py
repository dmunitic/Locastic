from .base_element import BaseElement


class TextField(BaseElement):
    """Text input field with optional associated error message span."""

    def __init__(self, page, locator_str, error_locator_str=None):
        super().__init__(page, locator_str)
        self._error_locator = (
            page.locator(error_locator_str) if error_locator_str else None
        )

    def input(self, text):
        self._locator.fill(text)

    def clear(self):
        self._locator.clear()

    def get_value(self):
        return self._locator.input_value()

    def get_placeholder(self):
        return self._locator.get_attribute("placeholder")

    def get_input_type(self):
        return self._locator.get_attribute("type")

    def has_error(self):
        if not self._error_locator:
            return False
        text = self._error_locator.text_content()
        return bool(text and text.strip())

    def get_error_message(self):
        if not self._error_locator:
            return ""
        return self._error_locator.text_content().strip()

    def error_is_visible(self):
        """Check if error element is actually visible (not hidden by CSS)."""
        if not self._error_locator:
            return False
        return self._error_locator.is_visible()
