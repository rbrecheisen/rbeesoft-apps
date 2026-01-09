from PySide6.QtWidgets import (
    QStackedWidget,
)
from rbeesoftapps.common.logmanager import LogManager
from rbeesoftapps.pyside6.ui.components.pages.page import Page

LOG = LogManager()


class PageLayout(QStackedWidget):
    def __init__(self) -> None:
        super(PageLayout, self).__init__()
        self._pages = {}

    def add_page(self, page: Page) -> None:
        if page.page_id() in self._pages.keys():
            raise ValueError(f'Page {page.page_id()} already added to page layout')
        self._pages[page.page_id()] = page
        self.addWidget(page)
        LOG.info(f'Added page {page.page_title()}')
        self.select_page(page.page_id())

    def page(self, page_id: str) -> Page:
        if not page_id in self._pages.keys():
            raise ValueError(f'Page {page_id} unknown')
        return self._pages[page_id]

    def select_page(self, page_id: str) -> None:
        if not page_id in self._pages.keys():
            raise ValueError(f'Page {page_id} unknown')
        self.setCurrentWidget(self._pages[page_id])
        LOG.info(f'Selected page {self._pages[page_id].page_title()}')