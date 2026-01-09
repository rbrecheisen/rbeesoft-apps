from PySide6.QtWidgets import (
    QStackedWidget,
)
from rbeesoftapps.pyside6.ui.components.pages.page import Page


class PageLayout(QStackedWidget):
    def __init__(self) -> None:
        super(PageLayout, self).__init__()
        self._pages = {}

    def add_page(self, page: Page) -> None:
        if page.page_id() in self._pages.keys():
            raise ValueError(f'Page {page.page_id()} already added to page layout')
        self._pages[page.page_id()] = page
        self.addWidget(page)

    def select_page(self, page_id: str) -> None:
        if not page_id in self._pages.keys():
            raise ValueError(f'Page {page_id} unknown')
        self.setCurrentWidget(self._pages[page_id])