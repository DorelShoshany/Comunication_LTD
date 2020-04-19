# data base model:
import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy import DateTime, func, ForeignKey
from application import db


class PackagesSectors(db.Model):
    id = Column(db.Integer, primary_key=True)
    packageId = db.Column('packageId', db.Integer, ForeignKey("Package.id"), nullable=True)
    sectorId = db.Column('sectorId', db.Integer, ForeignKey("Sectors.id"), nullable=True)
    creationDate = db.Column('creationDate', DateTime, default=func.now())
    price = Column(db.Integer)

    def __init__(self, id, packageId, sectorId, creationDate, price):
        self.id = id
        self.packageId = packageId
        self.sectorId = sectorId
        self.creationDate = creationDate
        self.price = price

