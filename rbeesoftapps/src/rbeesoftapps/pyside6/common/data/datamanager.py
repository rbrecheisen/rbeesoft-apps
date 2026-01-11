import os
import re
from rbeesoftapps.common.singleton import singleton
from rbeesoftapps.pyside6.common.data.session import Session
from rbeesoftapps.pyside6.common.data.models.filemodel import FileModel
from rbeesoftapps.pyside6.common.data.dto.file import File
from rbeesoftapps.pyside6.common.data.models.filesetmodel import FileSetModel
from rbeesoftapps.pyside6.common.data.dto.fileset import FileSet
from rbeesoftapps.pyside6.common.data.dto.dicomfile import DicomFile
from rbeesoftapps.pyside6.common.data.dto.dicomseries import DicomSeries


@singleton
class DataManager:
    def load_file(self, file_path: str) -> FileSet:
        with Session() as session:
            fileset_model_path = os.path.dirname(file_path)
            fileset_model_name = fileset_model_path.split(os.path.sep)[-1]
            fileset_model = FileSetModel(name=fileset_model_name, path=fileset_model_path)
            file_model_name = os.path.split(file_path)[1]
            file_model = FileModel(name=file_model_name, path=file_path, fileset=fileset_model)
            session.add(fileset_model)
            session.add(file_model)
            session.commit()
            file = File(file_model.id, file_model.name, file_model.path)
        return file

    def load_fileset(self, fileset_path: str, regexp: str='') -> FileSet:
        pattern = re.compile(regexp) if regexp else None
        with Session() as session:
            fileset_model_name = fileset_path.split(os.path.sep)[-1]
            fileset_model = FileSetModel(name=fileset_model_name, path=fileset_path)
            for file_name in os.listdir(fileset_path):
                if file_name.startswith('.'):
                    continue
                file_path = os.path.join(fileset_path, file_name)
                if os.path.isdir(file_path):
                    continue
                if pattern and not pattern.search(file_name):
                    continue
                file_path = os.path.join(fileset_path, file_name)
                file_model = FileModel(name=file_name, path=file_path, fileset=fileset_model)
                session.add(file_model)
            session.add(fileset_model)
            session.commit()
            fileset = FileSet(fileset_model.id, fileset_model.name, fileset_model.path)
            for file_model in fileset_model.files:
                file = File(file_model.id, file_model.name, file_model.path)
                fileset.add_file(file)
        return fileset
    
    def load_dicom_file(self, file_path: str) -> DicomFile:
        file = self.load_file(file_path)
        dicom_file = DicomFile(file)
        return dicom_file
    
    def load_dicom_series(self, fileset_path: str) -> DicomSeries:
        fileset = self.load_fileset(fileset_path)
        dicom_series = DicomSeries(fileset)
        return dicom_series