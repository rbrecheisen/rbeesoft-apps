from PySide6.QtWidgets import (
    QMainWindow,
)
from rbeesoftapps.pyside6.common.settings import Settings
from rbeesoftapps.common.logmanager import LogManager
from rbeesoftapps.pyside6.ui.components.dockwidgets.logdockwidget import LogDockWidget


class MainWindow(QMainWindow):
    def __init__(self, bundle_identifier: str, app_name: str) -> None:
        super(MainWindow, self).__init__()
        self._bundle_identifier = bundle_identifier
        self._app_name = app_name
        self._settings = Settings(self._bundle_identifier, self._app_name)
        self._log_manager = LogManager(self._app_name)
        self._log_dockwidget = None

    def settings(self):
        return self._settings

    def log_dockwidget(self):
        if not self._log_dockwidget:
            self._log_dockwidget = LogDockWidget()
            self._log_manager.add_listener(self._log_dockwidget)
        return self._log_dockwidget
