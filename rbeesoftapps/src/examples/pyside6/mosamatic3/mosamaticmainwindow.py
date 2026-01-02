from rbeesoftapps.pyside6.ui.mainwindow import MainWindow


class MosamaticMainWindow(MainWindow):
    def __init__(self) -> None:
        super(MosamaticMainWindow, self).__init__(
            bundle_identifier='nl.rbeesoft',
            app_name='mosamatic3'
        )
        self.settings().print()