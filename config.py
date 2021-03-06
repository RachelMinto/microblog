import websiteconfig # File for secret env variables

WTF_CSRF_ENABLED = True  #for web forms, activates cross-site request forgery prevention
SECRET_KEY = 'you-will-never-guess'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = websiteconfig.MAIL_USERNAME
MAIL_PASSWORD = websiteconfig.MAIL_PASSWORD

# administrator list
ADMINS = websiteconfig.ADMIN_EMAILS