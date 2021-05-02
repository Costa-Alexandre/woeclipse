from flask_login import UserMixin

from .website import db, login_manager


# Tables
user_event = db.Table(
    'user_event', db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')))


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
    # One-to-One relationship
    stats_id = db.Column(db.Integer, db.ForeignKey('stats.id'))
    # One-to-One relationship
    # avatar_id = db.Column(db.Integer, db.ForeignKey('avatar.id'))

    def __repr__(self):
        return f'<User {self.username}>'


class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # One-to-One relationship
    user_id = db.relationship(
        'User', backref="stats", lazy='select', uselist=False)
    team_name = db.Column(db.String(50), nullable=False)
    matches_w = db.Column(db.Integer, default=0)
    matches_d = db.Column(db.Integer, default=0)
    matches_l = db.Column(db.Integer, default=0)
    rank = db.Column(db.Integer, default=0)
    kills = db.Column(db.Integer, default=0)
    killed = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Stats from User.Id: {self.user_id} - Team: {self.team_name}>'

# class Avatar(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     # One-to-One relationship
#     user_id = db.relationship(
#         'User', backref="avatar", lazy='select', uselist=False)
#     img = db.Column(db.Text, unique=True, nullable=False)
#     name = db.Column(db.Text, nullable=False)
#     mime_type = db.Column(db.Text, nullable=False)

#     def __repr__(self):
#         return f'<Avatar from User.Id {self.user_id}>'

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(50), unique=True)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(
        db.String(600), default="No description to this event yet")
    users = db.relationship(
        'User', secondary=user_event, backref='events', lazy='select')

    def __repr__(self):
        return f'<Event {self.event_name}>'


# Connect flask login with the user records in our database:
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
