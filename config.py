import datetime
import os

import export

class Config(object):

    BASE_URL = 'https://127.0.0.1:5000'  # Running on localhost

    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"

    # DB:
    nameFileDB = "CommunicationLTDDB.db"
    basedir = os.path.dirname(os.path.abspath(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(basedir, nameFileDB))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT:
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
    JWT_TOKEN_LOCATION ='cookies'
    JWT_CSRF_CHECK_FORM = True


    # mail:

    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = 'dorel@ComunicationLTD.com'
    JWT_COOKIE_CSRF_PROTECT = False

    #TODO: use this!
    # CONST:
    LENGTH_OF_THE_SALT = 32
    LENGTH_OF_THE_PASSWORD = 7
    HISTORY_OF_THE_PASSWORDS = 3
    LOGIN_LIMIT_TRYING = 3
    TITLE_MSG_EMAIL_PASSWORD_RECOVERY = "Password Recovery - Communication LTD"
    TITLE_MSG_EMAIL_DEFAULT = 'Communication LTD'

    # consts for routes api :
    USER_NOT_FOUND = "User not fund "
    PASSWORD_NOT_CORRECT = "Password not correct "
    USER_FOUND = "User not fund "
    PASSWORD_CORRECT = "Password correct "
    VERIFY_HASH_EMAIL_WITH_DATE_SUCCESS = "verify email success"
    VERIFY_HASH_EMAIL_WITH_DATE_FAILED = "verify email failed"
    PASSWORD_CHANGE_SUCCESS = "Password change success "
    PASSWORD_CHANGE_FAILED = "Password change failed"
    PASSWORD_IS_COPY_OF_HISTORY = "Password is copy of history "

'''

    try:
        print("MAIL_PASSWORD:", os.environ['MAIL_PASSWORD'])
    except KeyError:
        print("Environment variable does not exist")

'''




