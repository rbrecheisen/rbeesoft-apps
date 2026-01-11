import os
import pydicom
import pydicom.errors
from typing import List
from rbeesoftapps.pyside6.core.data.fileset import FileSet
from rbeesoftapps.pyside6.core.data.dicomfile import DicomFile


class DicomSeries(FileSet):
    def __init__(self, path: str) -> None:
        super(DicomSeries, self).__init__(path)

    def load(self) -> bool:
        self.files().clear()
        if not os.path.isdir(self.path()):
            return False
        series_instance_uid = None
        for f in os.listdir(self.path()):
            f_path = os.path.join(self.path(), f)
            if f.startswith('.') or not os.path.isfile(f_path):
                continue
            file = DicomFile(f_path)
            if not file.load():
                continue
            suid = file.data().SeriesInstanceUID
            if series_instance_uid is None: series_instance_uid = suid
            if series_instance_uid != suid:
                raise ValueError('Mismatching series instance UIDs')
            self.files().append(file)
        return len(self.files()) > 0