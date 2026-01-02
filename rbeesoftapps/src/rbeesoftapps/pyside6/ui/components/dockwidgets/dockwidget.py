from PySide6.QtWidgets import (
    QDockWidget,
    QWidget,
)


class DockWidget(QDockWidget):
    def __init__(self, title: str, parent: QWidget=None) -> None:
        super(DockWidget, self).__init__(parent)
        self._title = title

    def title(self):
        return self._title