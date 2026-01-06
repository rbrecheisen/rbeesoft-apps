from rbeesoftapps.pyside6.ui.mainwindow import MainWindow


class MosamaticMainWindow(MainWindow):
    def __init__(self) -> None:
        super(MosamaticMainWindow, self).__init__(
            bundle_identifier='nl.rbeesoft',
            app_name='mosamatic3',
        )
        self.log().info(self.settings().to_string())
        self.add_page(
            None,
            '/data/dicom/anonymizer',
            'DICOM Anonyizer',
            'Data/Dicom',
        )