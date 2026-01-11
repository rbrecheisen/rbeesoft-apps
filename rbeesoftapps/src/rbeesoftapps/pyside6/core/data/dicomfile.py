import os
import pydicom
import pydicom.errors
from rbeesoftapps.pyside6.core.data.file import File


class DicomFile(File):
    def __init__(self, path: str) -> None:
        super(DicomFile, self).__init__(path)
        self._data = None

    def load(self) -> bool:
        self._data = None
        if os.path.isfile(self.path()):
            try:
                self._data = pydicom.dcmread(self.path())
                return True
            except pydicom.errors.InvalidDicomError:
                pass
        return False
        
    def data(self) -> pydicom.FileDataset:
        return self._data