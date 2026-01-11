import pydicom
import pydicom.errors
from rbeesoftapps.pyside6.common.data.dto.file import File


class DicomFile:
    def __init__(self, file: File) -> None:
        self._id, self._name, self._path = None, None, None
        if self.is_dicom(file):
            self._id, self._name, self._path = file.id(), file.name(), file.path()

    def id(self) -> str|None:
        return self._id
    
    def name(self) -> str|None:
        return self._name
    
    def path(self) -> str|None:
        return self._path

    def object(self, stop_before_pixels=False) -> pydicom.FileDataset|None:
        if self.path():
            return pydicom.dcmread(self.path(), stop_before_pixels=stop_before_pixels)
        return None
        
    def is_dicom(self, file: File) -> bool:
        try:
            pydicom.dcmread(file.path(), stop_before_pixels=True)
            return True
        except pydicom.errors.InvalidDicomError:
            return False