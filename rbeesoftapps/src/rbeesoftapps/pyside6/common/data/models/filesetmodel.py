import uuid
from typing import List
from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    relationship,
)
from rbeesoftapps.pyside6.common.data.models.basemodel import BaseModel


class FileSetModel(BaseModel):
    __tablename__ = '_filesetmodel'
    id: Mapped[int] = Column(
        '_id', 
        String, 
        primary_key=True, 
        default=lambda: str(uuid.uuid4()), 
        unique=True, 
        nullable=False
    )
    name: Mapped[str] = Column(
        '_name', 
        String, 
        nullable=False, 
        unique=False
    )
    path: Mapped[str] = Column(
        '_path', 
        String, 
        nullable=False, 
        unique=False
    )
    files: Mapped[List['FileModel']] = relationship('FileModel', back_populates='fileset', cascade='all, delete-orphan')