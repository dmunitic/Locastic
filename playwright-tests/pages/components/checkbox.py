from .base_element import BaseElement


class Checkbox(BaseElement):
    """Checkbox input element."""

    def check(self):
        self._locator.check()

    def uncheck(self):
        self._locator.uncheck()

    def is_checked(self):
        return self._locator.is_checked()
