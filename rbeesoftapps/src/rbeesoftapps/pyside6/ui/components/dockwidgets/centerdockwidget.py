from PySide6.QtWidgets import (
    QWidget,
)
from rbeesoftapps.pyside6.ui.components.dockwidgets.dockwidget import DockWidget
from rbeesoftapps.pyside6.ui.components.pages.pagelayout import PageLayout


class CenterDockWidget(DockWidget):
    def __init__(self, page_layout: PageLayout) -> None:
        super(CenterDockWidget, self).__init__()
        self._page_layout = page_layout
        self.init_layout()

    def page_layout(self):
        return self._page_layout

    def init_layout(self):
        self.setWidget(self.page_layout())
        self.setObjectName(self.__class__.__name__.lower())