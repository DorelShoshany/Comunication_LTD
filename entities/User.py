
# data base model:
import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy import DateTime, func, ForeignKey
from application import db


class User(db.Model):
    id = Column(db.Integer, primary_key=True)
    email = Column(db.String(45))
    password = Column(db.String(45))
    passwordChangedDate = db.Column('passwordChangedDate', DateTime, default=func.now())
    firstName = Column(db.String(45))
    lastName = Column(db.String(45))
    creationDate = db.Column('creationDate', DateTime, default=func.now())
    sectorId = db.Column('sectorId', db.Integer, ForeignKey("Sectors.id"), nullable=True)

    def __init__(self, id, email, password, passwordChangedDate, firstName, lastName, creationDate, sectorId):
        self.id = id
        self.email = email
        self.password = password
        self.passwordChangedDate = passwordChangedDate
        self.firstName = firstName
        self.lastName = lastName
        self.creationDate = creationDate
        self.sectorId = sectorId
