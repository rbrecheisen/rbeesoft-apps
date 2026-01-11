import os
from rbeesoftapps.pyside6.core.data.dicomseries import DicomSeries


class DicomSeriesList:
    def __init__(self, path: str) -> None:
        self._path = path

    def path(self) -> str:
        return self._path

    def load(self) -> bool:
        if not os.path.isdir(self.path()):
            return False
        for root, dirs, files in os.walk(self.path()):
            pass
        return True