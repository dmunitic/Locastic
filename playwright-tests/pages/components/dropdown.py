from .base_element import BaseElement


class Dropdown(BaseElement):
    """Select/dropdown element."""

    def select(self, value):
        self._locator.select_option(value=value)

    def select_by_label(self, label):
        self._locator.select_option(label=label)

    def get_selected_value(self):
        return self._locator.input_value()

    def get_options(self):
        return self._locator.locator("option").all_text_contents()
