from application import db
from config import Config
from entities.PackagesSectors import PackagesSectors
from entities.User import User
from entities.UserPasswordsHistory import UserPasswordsHistory



def save_new_user_to_db (user):
    try:
        print("save_new_user_to_db ",user.lockEndTime)
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


def save_new_packages_sectors_to_db (packagesSector):
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


def get_packages_sectors_from_db_by_sectorId(sectorId):
    return PackagesSectors.query.filter_by(id=sectorId)


def get_UserPasswordsHistory_by_user_id(userID):
    return UserPasswordsHistory.query.filter_by(userId=userID)


