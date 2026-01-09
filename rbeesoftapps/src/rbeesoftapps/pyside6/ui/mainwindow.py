from functools import partial
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
    QAction,
)
from rbeesoftapps.common.logmanager import LogManager
from rbeesoftapps.pyside6.ui.components.dockwidgets.centerdockwidget import CenterDockWidget
from rbeesoftapps.pyside6.ui.components.dockwidgets.logdockwidget import LogDockWidget
from rbeesoftapps.pyside6.ui.settings import Settings
from rbeesoftapps.pyside6.ui.components.pages.page import Page
from rbeesoftapps.pyside6.ui.components.pages.pagelayout import PageLayout
from rbeesoftapps.pyside6.ui.menumanager import MenuManager


class MainWindow(QMainWindow):
    def __init__(self, bundle_identifier: str, app_name: str, title: str, width: int, height: int) -> None:
        super(MainWindow, self).__init__()
        self._bundle_identifier = bundle_identifier
        self._app_name = app_name
        self._title = title
        self._width = width
        self._height = height
        self._settings = None
        self._log_manager = None
        self._menu_manager = MenuManager(self.menuBar())
        self._log_dockwidget = None
        self._page_layout = None
        self._center_dockwidget = None
        self.init_layout()

    # GETTERS

    def settings(self) -> Settings:
        if not self._settings:
            self._settings = Settings(self._bundle_identifier, self._app_name)
        return self._settings
    
    def log(self) -> LogManager:
        if not self._log_manager:
            self._log_manager = LogManager(self._app_name)
        return self._log_manager
    
    def menu_manager(self) -> MenuManager:
        if not self._menu_manager:
            self._menu_manager = MenuManager(self.menuBar())
        return self._menu_manager
    
    def page_layout(self) -> PageLayout:
        if not self._page_layout:
            self._page_layout = PageLayout()
        return self._page_layout
    
    def center_dockwidget(self) -> CenterDockWidget:
        if not self._center_dockwidget:
            self._center_dockwidget = CenterDockWidget(self.page_layout())
        return self._center_dockwidget

    def log_dockwidget(self) -> LogDockWidget:
        if not self._log_dockwidget:
            self._log_dockwidget = LogDockWidget()
            self._log_dockwidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
            self._log_dockwidget.setMaximumHeight(200)
            self.log().add_listener(self._log_dockwidget)
        return self._log_dockwidget
    
    # LAYOUT

    def init_app_menu(self) -> None:
        # This menu only shows up in the Windows version
        menu = self.menu_manager().create_menu('Application')
        menu_action = menu.addAction('Exit')
        menu_action.triggered.connect(self.close)
    
    def init_layout(self) -> None:
        self.setWindowTitle(self._title)
        self.init_app_menu()
        self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.center_dockwidget())
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.log_dockwidget())
        if not self.load_geometry_and_state():
            self.set_default_size_and_position()

    # PAGES

    def add_page(self, page: Page) -> None:
        self.page_layout().add_page(page)
        # Create menu for page
        menu = self.menu_manager().create_menu(page.menu_path())
        menu_action = menu.addAction(page.page_title())
        menu_action.triggered.connect(partial(self.navigate_to_page, page.page_id()))

    def page(self, page_id: str) -> Page:
        return self.page_layout().page(page_id)
    
    def navigate_to_page(self, page_id) -> None:
        self.page_layout().select_page(page_id)

    # LOAD/SAVE GEOMETRY AND STATE

    def load_geometry_and_state(self) -> bool:
        geometry = self.settings().get('mainwindow/geometry')
        state = self.settings().get('mainwindow/state')
        if isinstance(geometry, QByteArray) and self.restoreGeometry(geometry):
            if isinstance(state, QByteArray):
                self.restoreState(state)
            return True
        return False

    def save_geometry_and_state(self) -> None:
        self.settings().set('mainwindow/geometry', self.saveGeometry())
        self.settings().set('mainwindow/state', self.saveState())
        # TODO: Save page layout as well

    # POSITIONING AND SIZE

    def set_default_size_and_position(self) -> None:
        self.resize(self._width, self._height)
        self.center_window()

    def center_window(self) -> None:
        screen = QGuiApplication.primaryScreen().geometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(int(x), int(y))

    # CLOSING

    def closeEvent(self, event) -> None:
        self.save_geometry_and_state()
        super().closeEvent(event)