from typing import List
from rbeesoftapps.pyside6.common.data.dto.fileset import FileSet
from rbeesoftapps.pyside6.common.data.dto.dicomfile import DicomFile


class DicomSeries:
    def __init__(self, fileset: FileSet) -> None:
        self._id, self._name, self._path = None, None, None
        self._files = self.find_dicom_files(fileset)
        if len(self._files) > 0:
            self._id, self._name, self._path = fileset.id(), fileset.name(), fileset.path()

    def id(self) -> str|None:
        return self._id
    
    def name(self) -> str|None:
        return self._name
    
    def path(self) -> str|None:
        return self._path
    
    def files(self) -> List[DicomFile]:
        return self._files

    def find_dicom_files(self, fileset: FileSet) -> List[DicomFile]:
        series_instance_uid = None
        dicom_files = []
        for file in fileset.files():
            dicom_file = DicomFile(file)
            if dicom_file.id():
                suid = dicom_file.object().SeriesInstanceUID
                if series_instance_uid is None:
                    series_instance_uid = suid
                if not series_instance_uid == suid:
                    raise ValueError(f'Mismatching series instance UID!')
                dicom_files.append(dicom_file)
        return dicom_files