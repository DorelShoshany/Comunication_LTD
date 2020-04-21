from application import db
from entities.User import User


def save_new_user_to_db (user):
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except IOError:
        return False


def save_new_sector_to_db (sector):
    db.session.add(sector)
    db.session.commit()
    return True


def save_new_package_to_db (package):
    db.session.add(package)
    db.session.commit()
    return True


