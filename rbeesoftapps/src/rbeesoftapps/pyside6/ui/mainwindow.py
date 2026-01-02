from PySide6.QtWidgets import (
    QMainWindow,
)
from rbeesoftapps.pyside6.common.settings import Settings


class MainWindow(QMainWindow):
    def __init__(self, bundle_identifier: str, app_name: str) -> None:
        super(MainWindow, self).__init__()
        self._settings = Settings(bundle_identifier, app_name)

    def settings(self):
        return self._settings
