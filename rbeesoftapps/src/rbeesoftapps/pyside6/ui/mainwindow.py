from PySide6.QtCore import (
    Qt,
)
from PySide6.QtWidgets import (
    QMainWindow,
    QSizePolicy,
)
from PySide6.QtGui import (
    QGuiApplication,
)
from rbeesoftapps.pyside6.common.settings import Settings
from rbeesoftapps.common.logmanager import LogManager
from rbeesoftapps.pyside6.ui.components.dockwidgets.centerdockwidget import CenterDockWidget
from rbeesoftapps.pyside6.ui.components.dockwidgets.logdockwidget import LogDockWidget


class MainWindow(QMainWindow):
    def __init__(self, bundle_identifier: str, app_name: str) -> None:
        super(MainWindow, self).__init__()
        self._bundle_identifier = bundle_identifier
        self._app_name = app_name
        self._settings = Settings(self._bundle_identifier, self._app_name)
        self._log_manager = LogManager(self._app_name)
        self._log_dockwidget = None
        self._center_dockwidget = None
        self.init_layout()

    def settings(self):
        return self._settings
    
    def log_manager(self):
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
        self.load_geometry_and_state()

    def load_geometry_and_state(self):
        settings = self.settings()
        width = settings.get_int('mainwindow.width', 1024)
        height = settings.get_int('mainwindow.height', 768)
        if width and width > 0 and height and height > 0:
            self.set_default_size(width, height)
        else:
            self.set_default_size(1024, 768)

    def save_geometry_and_state(self):
        self.settings().set('mainwindow.width', self.size().width())
        self.settings().set('mainwindow.height', self.size().height())

    def set_default_size(self, width, height):
        self.resize(width, height)
        self.center_window()

    def center_window(self):
        screen = QGuiApplication.primaryScreen().geometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(int(x), int(y))

    def closeEvent(self, event):
        self.save_geometry_and_state()
        return super().closeEvent(event)