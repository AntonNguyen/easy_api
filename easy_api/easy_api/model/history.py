"""History model"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, TIMESTAMP
from sqlalchemy.orm import relation, backref

from datetime import datetime
from user import User

from easy_api.model.meta import Base

class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    api_call = Column(String(5000), nullable=False)
    created = Column(TIMESTAMP, nullable=False, default=datetime.now)
    
    user = relation(User, backref='history')

    def __init__(self, user_id, api_call):
        self.user_id = user_id
        self.api_call = api_call

    def __repr__(self):
        return "<History('%s')" % self.api_call