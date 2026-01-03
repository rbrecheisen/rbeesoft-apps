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
from rbeesoftapps.pyside6.ui.settings import Settings
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
        if not self.load_geometry_and_state():
            self.set_default_size_and_position()

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
        self.resize(1024, 768)
        self.center_window()

    def center_window(self):
        screen = QGuiApplication.primaryScreen().geometry()
        x = (screen.width() - self.geometry().width()) / 2
        y = (screen.height() - self.geometry().height()) / 2
        self.move(int(x), int(y))

    def closeEvent(self, event):
        self.save_geometry_and_state()
        return super().closeEvent(event)