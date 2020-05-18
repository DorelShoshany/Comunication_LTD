# data base model:
import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy import DateTime, func, ForeignKey
from application import db

# we can decide that each package can be related to more than one sector in different prices

class PackagesSectors(db.Model):
    __tablename__ = 'PackagesSectors'
    id = Column(db.Integer, primary_key=True)
    packageId = db.Column('packageId', db.Integer, ForeignKey("Packages.id"), nullable=True)
    sectorId = db.Column('sectorId', db.Integer, ForeignKey("Sectors.id"), nullable=True)
    name = db.Column('name', db.Integer, ForeignKey("Packages.name"), nullable=True)
    creationDate = db.Column('creationDate', DateTime, default=func.now())
    price = Column(db.Integer) # we assume each package can be sold in different costs to different sectors

    def __init__(self, packageId, sectorId, price, name):
        self.packageId = packageId
        self.sectorId = sectorId
        self.price = price
        self.name = name

    def __str__(self):
        print("PackageId: " + str(self.packageId) + ", SectorId: "+ str(self.sectorId) +", Price:"+ str(self.price))


