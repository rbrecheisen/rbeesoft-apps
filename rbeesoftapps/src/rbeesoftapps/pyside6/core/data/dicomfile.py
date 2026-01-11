import os
import pydicom
import pydicom.errors
from rbeesoftapps.pyside6.core.data.file import File


class DicomFile(File):
    def __init__(self, path: str) -> None:
        super(DicomFile, self).__init__(path)
        self._data = None
        self._series_instance_uid = None
        self._instance_number = None
        self._patient_id = None
        self._rows = None
        self._columns = None
        self._slice_thickness = None
        self._modality = None
        self._series_description = None
        self._manufacturer = None

    def load(self) -> bool:
        self._data = None
        if not os.path.isfile(self.path()):
            return False
        try:
            self._data = pydicom.dcmread(self.path())
            if 'SeriesInstanceUID' in self._data:
                self._series_instance_uid = self._data.SeriesInstanceUID
            if 'InstanceNumber' in self._data:
                self._instance_number = self._data.InstanceNumber
            if 'PatientID' in self._data:
                self._patient_id = self._data.PatientID
            if 'Rows' in self._data:
                self._rows = self._data.Rows
            if 'Columns' in self._data:
                self._columns = self._data.Columns
            if 'SliceThickness' in self._data:
                self._slice_thickness = self._data.SliceThickness
            if 'Modality' in self._data:
                self._modality = self._data.Modality
            if 'SeriesDescription' in self._data:
                self._series_description = self._data.SeriesDescription
            if 'Manufacturer' in self._data:
                self._manufacturer = self._data.Manufacturer
            return True
        except pydicom.errors.InvalidDicomError:
            return False
        
    def data(self) -> pydicom.FileDataset:
        return self._data
    
    def series_instance_uid(self) -> str:
        return self._series_instance_uid
    
    def instance_number(self) -> int|None:
        return int(self._instance_number) if self._instance_number else None
    
    def patient_id(self) -> str:
        return self._patient_id
    
    def rows(self) -> int|None:
        return int(self._rows) if self._rows else None
    
    def columns(self) -> int|None:
        return int(self._columns) if self._columns else None
    
    def slice_thickness(self) -> float|None:
        return float(self._slice_thickness) if self._slice_thickness else None
    
    def modality(self) -> str:
        return self._modality
    
    def series_description(self) -> str:
        return self._series_description
    
    def manufacturer(self) -> str:
        return self._manufacturer