
# data base model:
import datetime

from sqlalchemy import Column, ForeignKey

from application import db


class Sectors(db.Model):
    __tablename__ = 'Sectors'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(20))
    description = Column(db.String(20))

'''
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

'''

