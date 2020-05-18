# data base model:
import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy import DateTime, func, ForeignKey
from application import db


class UserPurchases(db.Model):
    __tablename__ = 'UserPurchases'
    id = Column(db.Integer, primary_key=True)
    userId = db.Column('userId', db.Integer, ForeignKey("User.id"), nullable=True)
    packagesSectorsId = db.Column('packagesSectorsId', db.Integer, ForeignKey("PackagesSectors.id"), nullable=True)
    name = Column('name', db.Integer, ForeignKey("PackagesSectors.name"), nullable=True)
    price = Column('price', db.Integer, ForeignKey("PackagesSectors.price"), nullable=True)
    date = db.Column('date', DateTime, default=func.now())

    def __init__(self, user_id, packagesSectorsId, price, name):
        self.userId = user_id
        self.packagesSectorsId = packagesSectorsId
        self.price = price
        self.name = name




