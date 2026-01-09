from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QSplitter,
    QLabel,
)


class Page(QWidget):
    def __init__(self, page_id: str, page_title: str, menu_path: str) -> None:
        super(Page, self).__init__()
        self._page_id = page_id
        self._page_title = page_title
        self._menu_path = menu_path
        self._splitter = None
        self._page_title_label = None
        self._property_widget = None
        self._main_widget = None
        self.init_layout()

    def init_layout(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 0, 0, 0)
        layout.addWidget(self.page_title_label(), 0, Qt.AlignTop)
        layout.addWidget(self.splitter(), 1)
        self.setLayout(layout)

    def page_id(self):
        return self._page_id
    
    def page_title(self):
        return self._page_title
    
    def menu_path(self):
        return self._menu_path
    
    def splitter(self):
        if not self._splitter:
            self._splitter = QSplitter(Qt.Horizontal, self)
            self._splitter.addWidget(self.property_widget())
            self._splitter.addWidget(self.main_widget())
            self._splitter.setStretchFactor(0, 0)
            self._splitter.setStretchFactor(1, 1)
        return self._splitter
    
    def page_title_label(self):
        if not self._page_title_label:
            self._page_title_label = QLabel(self.page_title())
            self._page_title_label.setStyleSheet('font-weight: bold; font-size: 16px;')
        return self._page_title_label
    
    def property_widget(self):
        if not self._property_widget:
            self._property_widget = QWidget()
            self._property_widget.setStyleSheet('background-color: red;')
        return self._property_widget
    
    def main_widget(self):
        if not self._main_widget:
            self._main_widget = QWidget()
            self._main_widget.setStyleSheet('background-color: blue;')
        return self._main_widget