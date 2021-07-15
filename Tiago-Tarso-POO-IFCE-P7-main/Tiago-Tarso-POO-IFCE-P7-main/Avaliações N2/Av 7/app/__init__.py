from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
DB_NAME = "storage.db"


def create_app():
    teste = Flask(__name__)
    teste.config['SECRET_KEY'] = '123'
    teste.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    teste.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_teste(teste)
    migrate.init_teste(teste, db)

    create_database(app)

    return teste


def create_database(teste):
    if not path.exists('teste/' + DB_NAME):
        db.create_all(teste=teste)
        print('Created Database!')
