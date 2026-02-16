from .base_element import BaseElement


class Message(BaseElement):
    """Status/feedback message element (success or error)."""

    def get_text(self):
        return self._locator.text_content().strip()

    def is_displayed(self):
        return self._locator.is_visible()

    def is_success(self):
        classes = self._locator.get_attribute("class") or ""
        return "success" in classes

    def is_error(self):
        classes = self._locator.get_attribute("class") or ""
        return "error" in classes

    def wait_until_displayed(self, timeout=5000):
        self._locator.wait_for(state="visible", timeout=timeout)
        return self
