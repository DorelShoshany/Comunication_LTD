
# data base model:

from sqlalchemy import Column, ForeignKey
from sqlalchemy import DateTime, func, ForeignKey
from application import db

#TODO: add user role 

class User(db.Model):
    __tablename__ = 'User'
    id = Column(db.Integer, primary_key=True)
    email = Column(db.String(45))
    password = Column(db.String(150))
    passwordChangedDate = db.Column('passwordChangedDate', DateTime, default=func.now())
    firstName = Column(db.String(45))
    lastName = Column(db.String(45))
    creationDate = db.Column('creationDate', DateTime, default=func.now())
    sectorId = db.Column('sectorId', db.Integer, ForeignKey("Sectors.id"), nullable=True) # We assume user belong only to one sector,
    invalidLoginAttempt = Column(db.Integer)
    lockEndTime = db.Column("lockEndTime", db.DateTime)


    def __init__(self, email, password, firstName, lastName, sectorId, lockEndTime=None):
        self.email = email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.sectorId = sectorId
        self.invalidLoginAttempt = 0
        if lockEndTime != None:
            self.lockEndTime = lockEndTime
        else:
            self.lockEndTime= None


    def __str__(self):
        return str(self.email)



