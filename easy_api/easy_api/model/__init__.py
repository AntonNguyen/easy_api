"""The application's model objects"""
from easy_api.model.meta import Session, Base
from easy_api.model.user import User


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
