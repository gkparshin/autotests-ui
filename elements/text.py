from playwright.sync_api import expect, Locator
from elements.base_element import BaseElement


class Text(BaseElement):
    @property
    def type_of(self) -> str:
        return "text"