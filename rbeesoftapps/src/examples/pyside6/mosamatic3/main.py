import sys

from PySide6 import QtWidgets

from examples.pyside6.mosamatic3.mosamaticmainwindow import MosamaticMainWindow


def main():
    QtWidgets.QApplication.setApplicationName('mosamatic3')
    app = QtWidgets.QApplication(sys.argv)
    window = MosamaticMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()