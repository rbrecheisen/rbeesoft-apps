from PySide6.QtWidgets import (
    QWidget,
)
from rbeesoftapps.pyside6.ui.components.dockwidgets.dockwidget import DockWidget


class CenterDockWidget(DockWidget):
    def __init__(self):
        super(CenterDockWidget, self).__init__()
        self._init_layout()

    def _init_layout(self):
        self.setWidget(QWidget())
        self.setObjectName(self.__class__.__name__.lower())