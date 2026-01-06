from PySide6.QtCore import (
    Qt,
    QByteArray,
)
from PySide6.QtWidgets import (
    QMainWindow,
    QSizePolicy,
)
from PySide6.QtGui import (
    QGuiApplication,
)
from rbeesoftapps.common.logmanager import LogManager
from rbeesoftapps.pyside6.ui.components.dockwidgets.centerdockwidget import CenterDockWidget
from rbeesoftapps.pyside6.ui.components.dockwidgets.logdockwidget import LogDockWidget
from rbeesoftapps.pyside6.ui.settings import Settings
from rbeesoftapps.pyside6.ui.pages.page import Page
from rbeesoftapps.pyside6.ui.menumanager import MenuManager


class MainWindow(QMainWindow):
    def __init__(self, bundle_identifier: str, app_name: str, width: int, height: int) -> None:
        super(MainWindow, self).__init__()
        self._bundle_identifier = bundle_identifier
        self._app_name = app_name
        self._width = width
        self._height = height
        self._settings = Settings(self._bundle_identifier, self._app_name)
        self._log_manager = LogManager(self._app_name)
        self._menu_manager = MenuManager(self.menuBar())
        self._log_dockwidget = None
        self._pages = {}
        self._center_dockwidget = None
        self.init_layout()

    def settings(self):
        """ Returns settings object for this main window """
        return self._settings
    
    def log(self):
        """ Returns log manager object for this main window """
        return self._log_manager
    
    def center_dockwidget(self):
        if not self._center_dockwidget:
            self._center_dockwidget = CenterDockWidget()
        return self._center_dockwidget

    def log_dockwidget(self):
        if not self._log_dockwidget:
            self._log_dockwidget = LogDockWidget()
            self._log_dockwidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
            self._log_dockwidget.setMaximumHeight(200)
            self._log_manager.add_listener(self._log_dockwidget)
        return self._log_dockwidget
    
    def init_layout(self):
        self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.center_dockwidget())
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.log_dockwidget())
        if not self.load_geometry_and_state():
            self.set_default_size_and_position()

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

    def load_geometry_and_state(self):
        geometry = self.settings().get('mainwindow/geometry')
        state = self.settings().get('mainwindow/state')
        if isinstance(geometry, QByteArray) and self.restoreGeometry(geometry):
            if isinstance(state, QByteArray):
                self.restoreState(state)
            return True
        return False

    def save_geometry_and_state(self):
        self.settings().set('mainwindow/geometry', self.saveGeometry())
        self.settings().set('mainwindow/state', self.saveState())

    def set_default_size_and_position(self):
        self.resize(self._width, self._height)
        self.center_window()

    def center_window(self):
        screen = QGuiApplication.primaryScreen().geometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(int(x), int(y))

    def closeEvent(self, event):
        self.save_geometry_and_state()
        return super().closeEvent(event)
