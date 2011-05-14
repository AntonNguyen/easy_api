"""User model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from easy_api.model.meta import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    url = Column(String(100))
    token = Column(String(100))
    description = Column(String(100))

    def __init__(self, url='', token='', description=''):
        self.url = url
        self.token = token
        self.description = description

    def __repr__(self):
        return "<User('%s')" % self.description