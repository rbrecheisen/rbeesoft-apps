import os
from sqlalchemy import create_engine
from rbeesoftapps.common.singleton import singleton
from rbeesoftapps.pyside6.common.data.models.basemodel import BaseModel


@singleton
class Engine:
    def __init__(self):
        url = os.getenv('RBEESOFTAPPS_TEST_DB_URL', 'sqlite:///db.sqlite3')
        connect_args = {}
        if url.startswith('sqlite:'):
            connect_args = {"check_same_thread": False}
        self._engine = create_engine(url, echo=False, connect_args=connect_args)
        BaseModel.metadata.create_all(self._engine)

    def get(self):
        return self._engine