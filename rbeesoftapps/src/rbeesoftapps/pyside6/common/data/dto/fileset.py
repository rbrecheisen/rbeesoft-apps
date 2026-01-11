from typing import List
from rbeesoftapps.pyside6.common.data.dto.file import File


class FileSet:
    def __init__(self, id: str, name: str, path: str) -> None:
        self._id = id
        self._name = name
        self._path = path
        self._files = []

    def id(self) -> str:
        return self._id
    
    def name(self) -> str:
        return self._name
    
    def path(self) -> str:
        return self._path

    def add_file(self, file: File) -> None:
        self._files.append(file)

    def files(self) -> List[File]:
        return self._files