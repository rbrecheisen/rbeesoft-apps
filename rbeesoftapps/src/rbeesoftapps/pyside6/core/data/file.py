class File:
    def __init__(self, path: str) -> None:
        self._path = path

    def path(self) -> str:
        return self._path
    
    def load(self) -> None:
        raise NotImplementedError()