from application import db
from entities.PackagesSectors import PackagesSectors
from entities.User import User


def save_new_user_to_db (user):
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except IOError:
        return False

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
