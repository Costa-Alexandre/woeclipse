# file to configure flask, loaded into our flask application
# using the line: app.config.from_pyfile("config.py") in website.py
from os import environ
import yaml

try:
    with open('app.yaml', "r") as f:
        data = yaml.load(f, Loader=yaml.BaseLoader)
    env_vars = data['env_variables']
    for k,v in env_vars.items():
        environ[k] = v

    SECRET_KEY = '123456'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:' + environ.get('DB_PASSWORD') + '@35.198.159.181/woeclipse'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

except:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# You can then set a different password for your production database in GitHub,
# by adding it as a repository secret, like with our google cloud credentials.
# Those passwords can then be added dynamically to app.yaml by the GitHub
# Action step called "Prepare Deployment" on line 36 of main.yaml.