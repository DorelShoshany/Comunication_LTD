# data base model:
import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy import DateTime, func, ForeignKey
from application import db


class UserPasswordsHistory(db.Model):
    __tablename__ = 'UserPasswordsHistory'
    id = Column(db.Integer, primary_key=True)
    userId = db.Column('userId', db.Integer, ForeignKey("User.id"), nullable=True)
    password = Column(db.String(150))
    creationDate = db.Column('creationDate', DateTime, default=func.now())
'''
    def __init__(self, id, userId, password, creationDate):
        self.id = id
        self.userId = userId
        self.password = password
        self.creationDate = creationDate
'''


