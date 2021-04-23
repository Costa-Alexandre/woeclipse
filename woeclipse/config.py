import os


SECRET_KEY = os.getenv('DB_SECRET')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{host}/{db}'.format(
                                                    user=DB_USER,
                                                    pw=DB_PASSWORD,
                                                    host=DB_HOST,
                                                    db=DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URL
