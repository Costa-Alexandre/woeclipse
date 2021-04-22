# file to configure flask, loaded into our flask application
# using the line: app.config.from_pyfile("config.py") in website.py
from os import environ

#
# You can then set a different password for your production database in GitHub,
# by adding it as a repository secret, like with our google cloud credentials.
# Those passwords can then be added dynamically to app.yaml by the GitHub
# Action step called "Prepare Deployment" on line 36 of main.yaml.
SECRET_KEY = environ.get('DB_PASSWORD')
SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://postgres:\
                        {SECRET_KEY}@35.198.159.181/woeclipse'
SQLALCHEMY_TRACK_MODIFICATIONS = False
