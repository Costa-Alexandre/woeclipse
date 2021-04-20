from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user,\
                        login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
# from datetime import datetime

app = Flask(__name__)
load_dotenv()
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

login_manager = LoginManager()  # initialize flask_login
login_manager.init_app(app)  # initialize flask_login with our app
login_manager.login_view = 'index'  # redirect route when @login_required fails


# Connect flask login with the user records in our database:
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    # birthday = db.Column(db.DateTime())
    country = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(80))
    is_admin = db.Column(db.Boolean, default=False)


# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        # Show the home page only to logged in users:
        return render_template('index.html', username=current_user.username)
    else:
        # If users aren't logged in they should be
        # redirected to the signin page:
        return render_template('index.html')


@app.route('/admin')
@login_required
def admin():
    if current_user.is_admin:
        return render_template('admin.html')
    else:
        return 'You are not authorized to view this page.'


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        # Run this when submitting the signup form:
        try:
            # Assign form values to variables to make working
            # with them easier later:
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            # birthday = datetime(request.form.get('birthday'))
            country = request.form.get('country')
            email = request.form.get('email')
            username = request.form.get('username')
            password = request.form.get('password')
            password_confirmation = request.form.get('password_confirmation')

            # Validations: Throw an error if anything is wrong
            # with the input parameters:
            if not email or not password or not username:
                raise ValueError('Email, username or password\
                                 parameter was missing.')

            if not password == password_confirmation:
                raise ValueError('The two passwords are not matching.')

            # Hash the password to be stored in the database
            # in an encrypted format:
            hashed_password = generate_password_hash(password, method='sha256')

            # Create a new use record in the database:
            new_user = User(first_name=first_name,
                            last_name=last_name,
                            country=country,
                            email=email,
                            username=username,
                            password=hashed_password)

            db.session.add(new_user)
            db.session.commit()

            # Login the user
            login_user(new_user)

            # Send the user to the home page after successful login:
            return redirect('/')
        except Exception as error_message:
            # Rerender the signup page and display an error
            # message if any of the code above failed:
            return render_template('signup.html',
                                   error="User could not be created.\
                                   " + str(error_message))
    else:
        # Run this when a user goes too the /signup route in the browser:
        return render_template('signup.html')


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        # Run this when submitting the signin form:
        try:
            # Assign form values to variables to make working
            # with them easier later:
            username = request.form.get('username')
            password = request.form.get('password')

            # Try to find a user record in the database with the
            # given email address:
            user = User.query.filter_by(username=username).first()

            # Make sure that the given password matches the encrypted
            # password of the user from the database:
            if user and check_password_hash(user.password, password):
                # If the use exists and the encrypted password matches,
                # login the user and send them to the home page:
                login_user(user)
                return redirect('/')
            else:
                # If no user with the given email address was found
                # or the password doesn't match throw an error:
                raise ValueError("Couldn't login with given login parameters.")
        except Exception:
            # Rerender the signin page with an error message
            # if anything goes wrong in the code above:
            return render_template('signin.html',
                                   error="Invalid username or password.")
    else:
        # Run this when a user goes too the /signin route in the browser:
        return render_template('signin.html')


@app.route('/signout')
@login_required
def signout():
    # Logout users and send them back to the signin page:
    logout_user()
    return redirect(url_for('index'))


# Run the server

if __name__ == "__main__":
    app.run(debug=True)
