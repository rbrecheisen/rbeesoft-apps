class File:
    def __init__(self, id: str, name: str, path: str) -> None:
        self._id = id
        self._name = name
        self._path = path

    def id(self) -> str:
        return self._id
    
    def name(self) -> str:
        return self._name
    
    def path(self) -> str:
        return self._path