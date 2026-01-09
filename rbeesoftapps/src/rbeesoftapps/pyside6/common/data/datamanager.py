import os
import re
from rbeesoftapps.common.singleton import singleton
from rbeesoftapps.pyside6.common.data.session import Session
from rbeesoftapps.pyside6.common.data.models.filemodel import FileModel
from rbeesoftapps.pyside6.common.data.models.filesetmodel import FileSetModel


@singleton
class DataManager:
    def load_file(self, file_path: str) -> FileSetModel:
        with Session() as session:
            fileset = FileSetModel(
                name=file_path,
                path=os.path.split(file_path)[0],
            )
            session.add(fileset)
            file = FileModel(
                name=os.path.split(file_path)[1],
                path=file_path,
                fileset=fileset,
            )
            session.add(file)
            session.commit()
        return fileset

    def load_fileset(self, fileset_path: str, regexp: str='') -> FileSetModel:
        """ Example regular expressions: 
            - ".dcm"        -> r"\.dcm$"
            - "L3_*.nii.gz" -> r"^L3_.\.nii\.gz$"
        """
        pattern = re.compile(regexp) if regexp else None
        with Session() as session:
            fileset = FileSetModel(
                name=fileset_path,
                path=fileset_path,
            )
            session.add(fileset)
            for file_name in os.listdir(fileset_path):
                if file_name.startswith('.'):
                    continue
                if pattern and not pattern.search(file_name):
                    continue
                file_path = os.path.join(fileset_path, file_name)
                file = FileModel(
                    name=file_name,
                    path=file_path,
                    fileset=fileset,
                )
                session.add(file)
            session.commit()
        return fileset