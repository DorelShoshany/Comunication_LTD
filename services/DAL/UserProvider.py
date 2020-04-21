from entities.User import User


def get_user_from_db_by_email(email):
    return User.query.filter_by(email=email ).first()


def get_user_from_db_by_id(userId):
    return User.query.filter_by(id=userId).first()