from rbeesoftapps.pyside6.ui.mainwindow import MainWindow


class MosamaticMainWindow(MainWindow):
    def __init__(self) -> None:
        super(MosamaticMainWindow, self).__init__(
            bundle_identifier='nl.rbeesoft',
            app_name='mosamatic3'
        )
        self.log_manager().info(f'Settings: {self.settings().print()}')
        self.set_default_size(1024, 768)