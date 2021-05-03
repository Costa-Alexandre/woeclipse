import os, random
from flask import render_template, url_for, request, redirect, current_app, send_from_directory
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from PIL import Image

from flask import Blueprint
from .website import db
from .models import Event, User, Avatar

AVATAR_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Checks if an extension is valid
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in AVATAR_ALLOWED_EXTENSIONS

def get_random_avatar():
    path = current_app.config['RANDOM_AVATAR_PATH']
    avatar_list = os.listdir(path)
    filename = avatar_list[random.randrange(len(avatar_list))]
    return path, filename

routes = Blueprint(
    'routes', __name__, static_folder='static', template_folder='templates')


# ........................................................................... #
# ............................... AUTH ROUTES ............................... #
# ........................................................................... #
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
            team_name = f"{username.capitalize()}'s Team"

            if not email or not password or not username:
                raise ValueError(
                    'Email, username or password parameter was missing.')

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
                            password=hashed_password,
                            team_name=team_name
                            )

            db.session.add(new_user)

            path, filename = get_random_avatar()
            avatar = Avatar(path=path, filename=filename)

            db.session.add(avatar)
            new_user.avatar = avatar

            db.session.commit()

            login_user(new_user)

            return redirect('/')

        except Exception as error_message:
            return render_template(
                'signup.html',
                error="User could not be created." + str(error_message))
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
                avatar = '/uploads/' + current_user.avatar.filename
                return redirect('/', avatar=avatar)
            else:
                raise ValueError("Couldn't login with given login parameters.")
        except Exception:
            return render_template(
                'signin.html', error="Invalid username or password.")
    else:
        return render_template('signin.html')


@routes.route('/signout')
@login_required
def signout():
    # Logout users and send them back to the signin page:
    logout_user()
    return redirect(url_for('routes.index'))

@routes.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    # Update user signup information
    
    if current_user.is_authenticated:
        user = current_user
        # avatar = current_user.avatar

        if request.method == 'POST':
            try:
                first_name = request.form.get('first_name').lower()
                last_name = request.form.get('last_name').lower()
                birthday = request.form.get('birthday')
                country = request.form.get('country').lower()
                password = request.form.get('password')
                password_confirmation = request.form.get('password_confirmation')
                team_name = request.form.get('team_name')
                avatar = request.files['avatar']

                if not password == password_confirmation:
                    raise ValueError('The two passwords are not matching.')

                # if avatar.filename == '':
                #     return redirect(request.url)

                if avatar and allowed_file(avatar.filename):
                    filename = secure_filename(avatar.filename)
                    upload_path = os.path.join(current_app.config['UPLOADS_PATH'], str(user.id))
                    if not os.path.exists(upload_path):
                        os.makedirs(upload_path)
                    avatar.save(os.path.join(upload_path, filename))
                    return redirect(url_for('routes.profile'))

            except Exception:
                return redirect(url_for('routes.profile'))
                            
        else:
            return render_template('edit_profile.html', user=user)

# --------------------------------------------------------------------------- #
# ----------------------------- MAIN ROUTES --------------------------------- #
# --------------------------------------------------------------------------- #
@routes.route('/')
def index():
    events = Event.query.limit(8).all()
    users = User.query.limit(8).all()

    if current_user.is_authenticated:
        return render_template(
            'index.html', events=events, users=users)
    else:
        return render_template(
            'index.html', events=events, users=users)


@routes.route('/users/<username>')
def public_profile(username):
    user = User.query.filter_by(username=username).first()
    # Show the user public profile:
    return render_template('public_profile.html', user=user)


@routes.route('/profile')
@login_required
def profile():
    if current_user.is_authenticated:
        user = current_user
        return render_template('profile.html', user=user)
    else:
        return render_template('signin.html')

@routes.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(current_app.config['UPLOADS_PATH'], filename)


# ########################################################################### #
# ######################## ADMIN PANEL ROUTES ############################### #
# ########################################################################### #
@routes.route('/admin')
def admin():
    if current_user.is_admin:
        return render_template('admin.html')
    else:
        return 'You are not authorized to view this page.'


@routes.route('/admin/events')
@login_required
def admin_events():
    if current_user.is_admin:
        events = Event.query.all()
        return render_template('admin_events.html', events=events)
    else:
        return 'You are not authorized to view this page.'


@routes.route('/admin/edit_event/<event_id>', methods=['POST', 'GET'])
@login_required
def edit_event(event_id):
    if current_user.is_admin:
        event = Event.query.filter_by(id=event_id).first()

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
            participants = event.users
            users = User.query.all()

            return render_template(
                'edit_event.html', event=event,
                participants=participants, users=users)
    else:
        return 'You are not authorized to view this page.'


@routes.route('/admin/delete_event/<event_id>')
@login_required
def delete_event(event_id):
    if current_user.is_admin:
        event = Event.query.filter_by(id=event_id).first()

        db.session.delete(event)
        db.session.commit()

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

            new_event = Event(
                event_name=event_name,
                date=event_date,
                description=event_description)

            db.session.add(new_event)
            db.session.commit()
            return redirect(url_for('routes.admin_events'))
        else:
            return redirect(url_for('routes.admin_events'))
    else:
        return 'You are not authorized to view this page.'


@routes.route('/admin/add_participant/<event_id>', methods=['POST', 'GET'])
@login_required
def add_participant(event_id):
    if current_user.is_admin:
        event = Event.query.filter_by(id=event_id).first()

        if request.method == 'POST':
            username = request.form.get('participants')
            participant = User.query.filter_by(username=username).first()
            print(event.event_name, participant.username)
            event.users.append(participant)

            db.session.commit()
            return redirect(url_for('routes.edit_event', event_id=event_id))
        else:
            participants = User.query.all()
            return render_template(
                'add_participant.html', participants=participants, event=event)
    else:
        return 'You are not authorized to view this page.'


@routes.route('/admin/remove_participant/<event_id>/<user_id>')
@login_required
def remove_participant(user_id, event_id):
    if current_user.is_admin:
        event = Event.query.filter_by(id=event_id).first()
        user = User.query.filter_by(id=user_id).first()
        event.users.remove(user)
        db.session.commit()
        return redirect(url_for('routes.edit_event', event_id=event_id))
    else:
        return 'You are not authorized to view this page.'
