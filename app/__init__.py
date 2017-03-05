from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

SQLALCHEMY_TRACK_MODIFICATIONS = False
from app import views, models # this syntax avoids circular import error