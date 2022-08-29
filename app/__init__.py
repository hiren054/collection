from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from os import path

db = SQLAlchemy()
ma = Marshmallow()
DB_NAME = "manage.db" 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'this_is_seceret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    #intialize the database
    db.init_app(app)
    ma.init_app(app)       

    #importing both blueprint from auth and views.py files
    from .views import views
    
    #registering blueprint
    app.register_blueprint(views,url_prefix='/')

    create_database(app)

    return app

def create_database(app):
    #check if database is exists and if not exists create the database
    if not path.exists('app/' + DB_NAME) : 
        db.create_all(app=app)
        print("databse created!")