from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QSplitter,
)


class Page(QWidget):
    def __init__(self, page_id: str, page_title: str, menu_path: str) -> None:
        super(Page, self).__init__()
        self._page_id = page_id
        self._page_title = page_title
        self._menu_path = menu_path
        self._splitter = QSplitter(Qt.Horizontal, self)
        self._splitter.addWidget(QWidget())
        self._splitter.addWidget(QWidget())
        self._splitter.setStretchFactor(0, 0)
        self._splitter.setStretchFactor(1, 1)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._splitter)
        self.setLayout(layout)

    def page_id(self):
        return self._page_id
    
    def page_title(self):
        return self._page_title
    
    def menu_path(self):
        return self._menu_path