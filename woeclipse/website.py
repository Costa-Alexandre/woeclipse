from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()

login_manager = LoginManager()
# redirect route when @login_required fails
login_manager.login_view = 'routes.signin'


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    login_manager.init_app(app)  # initialize flask_login with our app
    db.init_app(app)

    from .routes import routes
    app.register_blueprint(routes)

    return app


app = create_app()
