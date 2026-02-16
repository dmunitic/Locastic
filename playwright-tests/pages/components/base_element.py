class BaseElement:
    """Base class for all page components. Wraps a Playwright Locator."""

    def __init__(self, page, locator_str):
        self._page = page
        self._locator_str = locator_str
        self._locator = page.locator(locator_str)

    @property
    def locator(self):
        """Raw Playwright Locator for advanced usage."""
        return self._locator

    def is_visible(self):
        return self._locator.is_visible()

    def is_hidden(self):
        return self._locator.is_hidden()

    def is_enabled(self):
        return self._locator.is_enabled()

    def wait_for(self, state="visible", timeout=5000):
        self._locator.wait_for(state=state, timeout=timeout)
        return self

    def get_attribute(self, name):
        return self._locator.get_attribute(name)

    def bounding_box(self):
        """Returns element's bounding box for visual/layout assertions."""
        return self._locator.bounding_box()
