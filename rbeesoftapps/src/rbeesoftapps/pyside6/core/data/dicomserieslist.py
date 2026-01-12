import os
from rbeesoftapps.pyside6.core.data.dicomseries import DicomSeries
from rbeesoftapps.pyside6.core.data.dicomfile import DicomFile


class DicomSeriesList:
    def __init__(self, path: str) -> None:
        self._path = path
        self._dicom_series = []

    def path(self) -> str:
        return self._path

    def load(self) -> bool:
        if not os.path.isdir(self.path()):
            return False
        d = {}
        for root, dirs, files in os.walk(self.path()):
            for f in files:
                if f.startswith('._'):
                    continue
                f_path = os.path.join(root, f)
                if not DicomFile.is_dicom(f_path):
                    continue
                dicom_file = DicomFile(f_path)
                if not dicom_file.load():
                    continue
                series_instance_uid = dicom_file.series_instance_uid()
                if not series_instance_uid in d.keys():
                    d[series_instance_uid] = []
                d[series_instance_uid].append(dicom_file)
        for k, v in d.items():
            dicom_series = DicomSeries()
            for f in v:
                dicom_series.add_file(f)
            self._dicom_series.append(dicom_series)
        return True
    
    def print(self):
        for series in self._dicom_series:
            series.print_info()