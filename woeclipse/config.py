import os

SECRET_KEY = '123456'
DATABASE_PASSWORD = os.getenv('DB_PASSWORD')
DB_URL = 'postgresql+psycopg2://postgres:{pw}@35.198.159.181/woeclipse'.format(pw=DATABASE_PASSWORD)
SQLALCHEMY_DATABASE_URI = DB_URL

# 'postgresql+psycopg2://postgres:hBcszIsbavFpmOhB@35.198.159.181/woeclipse'
SQLALCHEMY_TRACK_MODIFICATIONS = False
