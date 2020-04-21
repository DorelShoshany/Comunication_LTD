import datetime
import os


class Config(object):
    BASE_URL = 'https://127.0.0.1:5000'  #Running on localhost


    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"

    nameFileDB = "CommunicationLTDDB.db"
    basedir = os.path.dirname(os.path.abspath(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(basedir, nameFileDB))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = 'super-secret' # TODO: change this!
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
    JWT_TOKEN_LOCATION ='cookies'
    JWT_CSRF_CHECK_FORM = True

    LENGTH_OF_THE_SALT = 32
    LENGTH_OF_THE_PASSWORD = 10
    HISTORY_OF_THE_PASSWORDS = 3
