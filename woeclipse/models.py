from flask_login import UserMixin, LoginManager

from .website import db, app


# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), default="John")
    last_name = db.Column(db.String(50), default="Doe")
    birthday = db.Column(db.String(50), default="2000-01-01")
    country = db.Column(db.String(50), default='Germany')
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


class Stats(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(50))
    matches_w = db.Column(db.Integer, default=0)
    matches_d = db.Column(db.Integer, default=0)
    matches_l = db.Column(db.Integer, default=0)
    rank = db.Column(db.Integer, default=0)
    kills = db.Column(db.Integer, default=0)
    killed = db.Column(db.Integer, default=0)


login_manager = LoginManager()  # initialize flask_login
login_manager.init_app(app)  # initialize flask_login with our app
login_manager.login_view = 'index'  # redirect route when @login_required fails


# Connect flask login with the user records in our database:
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
