from PySide6.QtCore import (
    Qt,
)
from PySide6.QtWidgets import (
    QMainWindow,
)
from rbeesoftapps.common.logmanager import LogManager
from rbeesoftapps.pyside6.ui.components.dockwidgets.logdockwidget import LogDockWidget
from rbeesoftapps.pyside6.ui.settings import Settings
from rbeesoftapps.pyside6.ui.pages.page import Page
from rbeesoftapps.pyside6.ui.menumanager import MenuManager


class MainWindow(QMainWindow):
    def __init__(self, bundle_identifier: str, app_name: str) -> None:
        super(MainWindow, self).__init__()
        self._bundle_identifier = bundle_identifier
        self._app_name = app_name
        self._settings = Settings(self._bundle_identifier, self._app_name)
        self._log_manager = LogManager(self._app_name)
        self._menu_manager = MenuManager(self.menuBar())
        self._log_dockwidget = None
        self._pages = {}
        self.init_layout()

    def settings(self):
        """ Returns settings object for this main window """
        return self._settings
    
    def log(self):
        """ Returns log manager object for this main window """
        return self._log_manager

    def log_dockwidget(self):
        if not self._log_dockwidget:
            self._log_dockwidget = LogDockWidget()
            self._log_manager.add_listener(self._log_dockwidget)
        return self._log_dockwidget
    
    def init_layout(self):
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.log_dockwidget())

    def add_page(self, page: Page, page_id: str, page_title: str, menu_path: str) -> None:
        if page_id in self._pages.keys():
            raise Exception(f'Page with ID {page_id} already added to main window')
        self._pages[page_id] = {
            'page_title': page_title,
            'menu_path': menu_path,
            'page': page,
        }
        self._menu_manager.create_menu(menu_path)

    def page(self, page_id: str, key='page') -> Page:
        if not page_id in self._pages.keys():
            raise Exception(f'Page with ID {page_id} does not exist')
        if not key in self._pages[page_id]:
            raise Exception(f'Key {key} does not exist in dictionary for {page_id}')
        return self._pages[page_id][key]