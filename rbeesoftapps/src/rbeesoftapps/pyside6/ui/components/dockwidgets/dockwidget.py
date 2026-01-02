from PySide6.QtWidgets import (
    QDockWidget,
)


class DockWidget(QDockWidget):
    def __init__(self, title: str):
        super(DockWidget, self).__init__()
        self._title = title

    def title(self):
        return self._title