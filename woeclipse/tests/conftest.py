import pytest
from woeclipse.website import create_app
from woeclipse.models import User, Avatar, Event
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope='module')
def new_user():
    user = User(id=999, first_name='Pie', last_name='Testt',
                email='test@pytest.com', username='pytester',
                password='pytestpass', birthday='2000-01-01')
    return user


@pytest.fixture(scope='module')
def avatar():
    avatar = Avatar(filename='img.png')
    return avatar


@pytest.fixture(scope='module')
def new_event():
    event = Event(
        event_name='Tournment 2021', date="2000-01-01",
        description='This is an event')
    return event


@pytest.fixture(scope='module')
def test_client():
    app = create_app()

    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def app():
    app = create_app()
    return app
