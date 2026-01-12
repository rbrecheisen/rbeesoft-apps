import os
import pydicom
import pydicom.errors
from typing import List
from rbeesoftapps.pyside6.core.data.fileset import FileSet
from rbeesoftapps.pyside6.core.data.dicomfile import DicomFile


class DicomSeries(FileSet):
    def __init__(self, path: str=None) -> None:
        super(DicomSeries, self).__init__(path)
        self._series_instance_uid = None
        self._patient_id = None
        self._nr_slices = None
        self._slice_thickness = None
        self._rows = None
        self._columns = None
        self._modality = None
        self._series_description = None
        self._manufacturer = None

    def load(self) -> bool:
        if not self.path():
            raise ValueError('Path is not specified')
        if not os.path.isdir(self.path()):
            return False
        for f in os.listdir(self.path()):
            f_path = os.path.join(self.path(), f)
            if f.startswith('._') or not os.path.isfile(f_path):
                continue
            file = DicomFile(f_path)
            self.add_file(file)
        self._nr_slices = len(self.files())
        return self._nr_slices > 0
    
    def add_file(self, file) -> None:
        if not file.load():
            print(f'Error loading file: {file.path()}')
            return
        suid = file.series_description()
        if self._series_instance_uid is None: self._series_instance_uid = []
        if suid not in self._series_instance_uid: self._series_instance_uid.append(suid)
        # if self._series_instance_uid != suid:
        #     raise ValueError('Mismatching series instance UIDs')
        patient_id = file.patient_id()
        if self._patient_id is None: self._patient_id = []
        if patient_id not in self._patient_id: self._patient_id.append(patient_id)
        # if self._patient_id != patient_id:
        #     raise ValueError('Mismatching patient IDs')
        slice_thickness = file.slice_thickness()
        if self._slice_thickness is None: self._slice_thickness = []
        if slice_thickness not in self._slice_thickness: self._slice_thickness.append(slice_thickness)
        # if self._slice_thickness != slice_thickness:
        #     raise ValueError('Mismatching slice thicknesses')
        rows = file.rows()
        if self._rows is None: self._rows = []
        if rows not in self._rows: self._rows.append(rows)
        # if self._rows != rows:
        #     raise ValueError('Mismatching rows')
        columns = file.columns()
        if self._columns is None: self._columns = []
        if columns not in self._columns: self._columns.append(columns)
        # if self._columns != columns:
        #     raise ValueError('Mismatching columns')
        modality = file.modality()
        if self._modality is None: self._modality = []
        if modality not in self._modality: self._modality.append(modality)
        # if self._modality != modality:
        #     raise ValueError('Mismatching modalities')
        series_description = file.series_description()
        if self._series_description is None: self._series_description = []
        if series_description not in self._series_description: self._series_description.append(series_description)
        # if self._series_description != series_description:
        #     raise ValueError('Mismatching series descriptions')
        manufacturer = file.manufacturer()
        if self._manufacturer is None: self._manufacturer = []
        if manufacturer not in self._manufacturer: self._manufacturer.append(manufacturer)
        # if self._manufacturer != manufacturer:
        #     raise ValueError('Mismatching scanner manufacturers')
        self.files().append(file)

    def print_info(self):
        text =  f'series_instance_uid={self._series_instance_uid}, '
        text += f'patient_id={self._patient_id}, '
        text += f'nr_slices={self._nr_slices}, '
        text += f'slice_thickness={self._slice_thickness}, '
        text += f'rows={self._rows}, '
        text += f'columns={self._columns}, '
        text += f'modality={self._modality}, '
        text += f'series_description={self._series_description}, '
        text += f'manufacturer={self._manufacturer}'
        print(text)