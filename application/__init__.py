from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
db.init_app(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
mail = Mail(app)

from application import routesHtml, routesApi


@app.before_first_request
def create_tables():
    db.create_all()

'''
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('db created!')
    
    
@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('db drop all!')


@app.cli.command('db_seed')
def db_seed():
    packages = Packages (name="Packages for singels")
    db.session(packages)
    db.session.commit()




'''
