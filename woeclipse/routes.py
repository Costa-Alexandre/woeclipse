from flask import render_template, url_for, request, redirect
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from flask import Blueprint
from .website import db
from .models import Event, User, Stats


routes = Blueprint('routes', __name__, static_folder='static',
                   template_folder='templates')


# Routes
@routes.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html', username=current_user.username)
    else:
        return render_template('index.html')


@routes.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        try:
            first_name = request.form.get('first_name').lower()
            last_name = request.form.get('last_name').lower()
            birthday = request.form.get('birthday')
            country = request.form.get('country').lower()
            email = request.form.get('email').lower()
            username = request.form.get('username').lower()
            password = request.form.get('password')
            password_confirmation = request.form.get('password_confirmation')

            if not email or not password or not username:
                raise ValueError('Email, username or password\
                                 parameter was missing.')

            if not password == password_confirmation:
                raise ValueError('The two passwords are not matching.')

            hashed_password = generate_password_hash(password, method='sha256')

            # Create a new use record in the database:
            new_user = User(first_name=first_name,
                            last_name=last_name,
                            birthday=birthday,
                            country=country,
                            email=email,
                            username=username,
                            password=hashed_password)

            db.session.add(new_user)
            db.session.commit()

            # Create stats entry for newly created user
            team_name = f"{new_user.username.capitalize()}'s Team"
            new_stats_entry = Stats(user_id=new_user.id, team_name=team_name)

            db.session.add(new_stats_entry)
            db.session.commit()
            login_user(new_user)

            return redirect('/')

        except Exception as error_message:
            return render_template('signup.html',
                                   error="User could not be created.\
                                   " + str(error_message))
    else:
        # When request = GET:
        return render_template('signup.html')


@routes.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':

        try:
            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                return redirect('/')
            else:
                raise ValueError("Couldn't login with given login parameters.")
        except Exception:
            return render_template('signin.html',
                                   error="Invalid username or password.")
    else:
        return render_template('signin.html')


@routes.route('/signout')
@login_required
def signout():
    # Logout users and send them back to the signin page:
    logout_user()
    return redirect(url_for('routes.index'))


@routes.route('/user/<username>')
def public_profile(username):
    user = User.query.filter_by(username=username).first()
    stats = Stats.query.filter_by(user_id=user.id).first()
    # Show the user public profile:
    return render_template('profile.html',
                           username=current_user.username,
                           first_name=current_user.first_name,
                           last_name=current_user.last_name,
                           country=current_user.country,
                           team_name=stats.team_name,
                           matches_w=stats.matches_w,
                           matches_d=stats.matches_d,
                           matches_l=stats.matches_l,
                           rank=stats.rank,
                           kills=stats.kills,
                           killed=stats.killed
                           )


@routes.route('/profile')
@login_required
def profile():
    if current_user.is_authenticated:
        stats = Stats.query.filter_by(user_id=current_user.id).first()
        return render_template('profile.html',
                               username=current_user.username,
                               first_name=current_user.first_name,
                               last_name=current_user.last_name,
                               country=current_user.country,
                               team_name=stats.team_name,
                               matches_w=stats.matches_w,
                               matches_d=stats.matches_d,
                               matches_l=stats.matches_l,
                               rank=stats.rank,
                               kills=stats.kills,
                               killed=stats.killed
                               )
    else:
        return render_template('signin.html')

# ADMIN ROUTES
@routes.route('/admin')
def admin():
    if current_user.is_admin:
        return render_template('admin.html', username=current_user.username)
    else:
        return 'You are not authorized to view this page.'

@routes.route('/admin/events')
@login_required
def admin_events():
    if current_user.is_admin:
        events = Event.query.all()
        return render_template('admin_events.html', username=current_user.username, events=events)
    else:
        return 'You are not authorized to view this page.'

@routes.route('/admin/edit_event/<event_id>', methods=['POST', 'GET'])
@login_required
def edit_event(event_id):
    if current_user.is_admin:
        event = Event.query.filter_by(id = event_id).first()

        if request.method == 'POST':
            # Get values from form
            new_event_name = request.form.get('event_name')
            new_event_date = request.form.get('event_date')
            new_event_description = request.form.get('event_description')

            # print(new_event_name, new_event_date, new_event_description)
            # make edits
            event.event_name = new_event_name
            event.date = new_event_date
            event.description = new_event_description

            db.session.commit()
            return redirect(url_for('routes.admin_events'))

        else:
            # When request is GET
            return render_template('edit_event.html', username=current_user.username, event=event)
    else:
        return 'You are not authorized to view this page.'

@routes.route('/admin/delete_event/<event_id>')
@login_required
def delete_event(event_id):
    if current_user.is_admin:
        event = Event.query.filter_by(id = event_id).first()
        try: 
            db.session.delete(event)
            db.session.commit()
            return redirect(url_for('routes.admin_events'))
        except Exception:
            db.session.rollback()
            return redirect(url_for('routes.admin_events'))
    else:
        return 'You are not authorized to view this page.'

@routes.route('/admin/create_event', methods=['POST', 'GET'])
@login_required
def create_event():
    if current_user.is_admin:
        if request.method == 'POST':
            event_name = request.form.get('event_name')
            event_date = request.form.get('event_date')
            event_description = request.form.get('event_description')

            new_event = Event(event_name=event_name, date=event_date, description=event_description)

            db.session.add(new_event)
            db.session.commit()
            return redirect(url_for('routes.admin_events'))
        else:
            return redirect(url_for('routes.admin_events'))
    else:
        return 'You are not authorized to view this page.'