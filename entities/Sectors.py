

from sqlalchemy import Column, ForeignKey
from sqlalchemy import DateTime, func, ForeignKey
from application import db


class Sectors(db.Model):
    __tablename__ = 'Sectors'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(20))
    description = Column(db.String(20))

    def __init__(self, name, description):
        self.name = name
        self.description = description



