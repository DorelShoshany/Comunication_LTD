import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    nameFileDB = "CommunicationLTDDB.db"
    basedir = os.path.dirname(os.path.abspath(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(basedir, nameFileDB))
    SQLALCHEMY_TRACK_MODIFICATIONS = False