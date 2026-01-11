import uuid
from sqlalchemy import (
    Column, 
    String, 
    ForeignKey,
)
from sqlalchemy.orm import (
    Mapped, 
    relationship,
)
from rbeesoftapps.pyside6.common.data.models.basemodel import BaseModel


class FileModel(BaseModel):
    __tablename__ = '_filemodel'
    id: Mapped[str] = Column(
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
    fileset: Mapped['FileSetModel'] = relationship('FileSetModel', back_populates='files')
    fileset_id: Mapped[str] = Column(
        '_filesetmodel_id', 
        ForeignKey('_filesetmodel._id', ondelete='CASCADE'), 
        nullable=False, 
        index=True
    )