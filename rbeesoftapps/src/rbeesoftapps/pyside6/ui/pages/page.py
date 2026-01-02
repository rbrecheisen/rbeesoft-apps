from PySide6.QtWidgets import (
    QWidget,
)


class Page(QWidget):
    def __init__(self, parent: QWidget=None) -> None:
        super(Page, self).__init__(parent)