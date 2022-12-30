import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'database.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(12).hex()
JWT_SECRET_KEY = "12's"