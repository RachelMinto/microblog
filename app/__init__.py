from flask import Flask

app = Flask(__name__)
from app import views # this syntax avoids circular import error