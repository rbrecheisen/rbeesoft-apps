import os
from rbeesoftapps.pyside6.core.loaders.loader import Loader
from rbeesoftapps.pyside6.core.data.file import File


class FileLoader(Loader):
    def __init__(self, path: str) -> None:
        super(FileLoader, self).__init__(path)

    def load(self) -> File|None:
        if not os.path.isfile(self.path()) and not os.path.isdir(self.path()):
            return None