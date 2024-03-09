from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, MetaData
from .base import Base
from sqlalchemy.orm import relationship
from datetime import datetime

metadata = MetaData()

class User(Base):
    __tablename__ = 'users'
    metadata = metadata
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    token = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    children = relationship('Child', back_populates='User')

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.token = self.id+1

class Child(Base):
    __tablename__ = 'child'
    metadata = metadata
    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, index=True)
    username = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


