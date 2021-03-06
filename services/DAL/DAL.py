from application import db
from config import Config
from entities.PackagesSectors import PackagesSectors
from entities.User import User
from entities.UserPasswordsHistory import UserPasswordsHistory
from entities.UserPurchases import UserPurchases


def save_new_purchase_to_db (UserPurchases):
    db.session.add(UserPurchases)
    db.session.commit()
    return True


def get_purchases_by_user_id(user_id):
    return UserPurchases.query.filter_by(userId=user_id)


def save_new_user_to_db (user):
    try:
        #db.session.execute("select * form User where name = %s" % ' ')
        db.session.add(user)
        db.session.commit()
        return True
    except IOError:
        return False


def save_user_password_history_to_db(user):
    userId = user.id
    password = user.password
    userPasswordsHistory = UserPasswordsHistory(userId=userId, password=password)
    db.session.add(userPasswordsHistory)
    db.session.commit()
    return True


def save_new_packages_sectors_to_db(packagesSector):
    db.session.add(packagesSector)
    db.session.commit()
    return True


def save_new_sector_to_db (sector):
    db.session.add(sector)
    db.session.commit()
    return True


def save_new_package_to_db (package):
    db.session.add(package)
    db.session.commit()
    return True


def get_packages_sectors_from_db_by_sector_id(sectorId):
    return PackagesSectors.query.filter_by(sectorId=sectorId)


def get_UserPasswordsHistory_by_user_id(userID):
    return UserPasswordsHistory.query.filter_by(userId=userID)


