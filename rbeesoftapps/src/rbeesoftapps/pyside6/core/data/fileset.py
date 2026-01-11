from typing import List
from rbeesoftapps.pyside6.core.data.file import File


class FileSet:
    def __init__(self, path: str) -> None:
        self._path = path
        self._files = []

    def path(self) -> str:
        return self._path
    
    def files(self) -> List[File]:
        return self._files
    
    def load(self) -> bool:
        raise NotImplementedError()