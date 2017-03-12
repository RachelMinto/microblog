from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
from flask_login import LoginManager
from config import basedir

import application


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

SQLALCHEMY_TRACK_MODIFICATIONS = False
from app import views, models # this syntax avoids circular import error

