# data base model:
import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy import DateTime, func, ForeignKey
from application import db


class UserPurchases(db.Model):
    id = Column(db.Integer, primary_key=True)
    userId = db.Column('userId', db.Integer, ForeignKey("User.id"), nullable=True)
    packageId = db.Column('packageId', db.Integer, ForeignKey("Package.id"), nullable=True)
    price = Column(db.Integer)
    date = db.Column('date', DateTime, default=func.now())

    def __init__(self, id, userId, packageId, price, date):
        self.id = id
        self.userId = userId
        self.packageId = packageId
        self.price = price
        self.date = date

