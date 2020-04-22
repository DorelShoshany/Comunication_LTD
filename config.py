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


    #TODO: use this!
    # CONST:
    LENGTH_OF_THE_SALT = 32
    LENGTH_OF_THE_PASSWORD = 10
    HISTORY_OF_THE_PASSWORDS = 3
    LOGIN_LIMIT_TRYING = 3
    TITLE_MSG_EMAIL = "Password Recovery - Communication LTD"

'''

    try:
        print("MAIL_PASSWORD:", os.environ['MAIL_PASSWORD'])
    except KeyError:
        print("Environment variable does not exist")

'''




