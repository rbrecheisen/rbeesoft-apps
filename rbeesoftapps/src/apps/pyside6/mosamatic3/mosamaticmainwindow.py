import apps.pyside6.mosamatic3.resources.mosamatic3_rc
from PySide6.QtGui import QIcon
from rbeesoftapps.pyside6.ui.mainwindow import MainWindow
from rbeesoftapps.pyside6.ui.components.pages.page import Page


class MosamaticMainWindow(MainWindow):
    def __init__(self) -> None:
        super(MosamaticMainWindow, self).__init__(
            bundle_identifier='nl.rbeesoft',
            app_name='mosamatic3',
            title='Mosamatic',
            width=1024,
            height=768,
            app_icon=QIcon(':/icons/mosamatic3.ico'),
        )
        self.log().info(self.settings().to_string())
        self.add_page(
            page=Page(
                page_id='/data/dicom/anonymizer',
                page_title='DICOM Anonymizer',
                menu_path='Data/Dicom',
            ),
        )        