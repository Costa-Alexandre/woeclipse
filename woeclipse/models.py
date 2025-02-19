from flask_login import UserMixin

from woeclipse.website import db, login_manager


# Tables

# Link Table USER EVENT
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
    avatar = db.relationship(
        'Avatar', backref='user', lazy='select', uselist=False)
    team_name = db.Column(db.String(50), nullable=False, default='New Team')
    matches_w = db.Column(db.Integer, default=0)
    matches_d = db.Column(db.Integer, default=0)
    matches_l = db.Column(db.Integer, default=0)
    kills = db.Column(db.Integer, default=0)
    killed = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.username}>'

    def points(self):
        """ return and int representing the total points based in the
        points_system list
        """
        points_system = [
            3,
            1,
            0,
            0.2,
            -0.1
        ]
        stats = [
            self.matches_w,
            self.matches_d,
            self.matches_l,
            self.kills,
            self.killed
        ]
        points = 0
        for i in range(len(stats)):
            points += stats[i] * points_system[i]
        return int(round(points, 0))


# TODO: delete user + avatar cascading
class Avatar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    filename = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.filename


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(50), unique=True)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(
        db.String(600), default="No description to this event yet")
    users = db.relationship(
        'User', secondary=user_event, backref='events', lazy='select')
    filename = filename = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Event {self.event_name}>'


# Connect flask login with the user records in our database:
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
