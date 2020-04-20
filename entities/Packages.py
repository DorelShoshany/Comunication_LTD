# data base model:
import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy import DateTime, func, ForeignKey
from application import db

class Packages(db.Model):
    __tablename__ = 'Packages'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(20))
    creationDate = db.Column('creationDate', DateTime, default=func.now())

'''
    def __init__(self, id, name, creationDate):
        self.id = id
        self.name = name
        self.creationDate = creationDate
'''

