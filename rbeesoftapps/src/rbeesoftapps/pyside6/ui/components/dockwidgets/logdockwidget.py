from PySide6.QtWidgets import (
    QWidget,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QLabel,
)
from rbeesoftapps.common.logmanagerlistener import LogManagerListener
from rbeesoftapps.pyside6.ui.components.dockwidgets.dockwidget import DockWidget


class LogDockWidget(DockWidget, LogManagerListener):
    def __init__(self, title: str='Output log'):
        super(LogDockWidget, self).__init__(title)
        self._title_label = None
        self._text_edit = None
        self._clear_logs_button = None
        self.init_layout()

    def title_label(self):
        if not self._title_label:
            self._title_label = QLabel(self.title())
        return self._title_label

    def text_edit(self):
        if not self._text_edit:
            self._text_edit = QTextEdit()
        return self._text_edit
    
    def clear_logs_button(self):
        if not self._clear_logs_button:
            self._clear_logs_button = QPushButton('Clear log')
            self._clear_logs_button.clicked.connect(self.handle_clear_logs_button)
        return self._clear_logs_button
    
    def init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit())
        layout.addWidget(self.clear_logs_button())
        container = QWidget()
        container.setLayout(layout)
        self.setWindowTitle(self.title_label().text())
        self.setWidget(container)

    # HELPERS

    def add_line(self, line):
        self.text_edit().insertPlainText(line + '\n')
        self.move_to_end()

    def move_to_end(self):
        cursor = self.text_edit().textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        self.text_edit().setTextCursor(cursor)
        self.text_edit().ensureCursorVisible()

    # EVENTS

    def handle_clear_logs_button(self):
        self.text_edit().clear()

    # implements(LogManagerListener)
    def new_message(self, message):
        self.add_line(message)