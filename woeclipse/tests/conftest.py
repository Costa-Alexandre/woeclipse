import pytest
from woeclipse.website import create_app
from woeclipse.models import User
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope='module')
def new_user():
    user = User(first_name='Pie', last_name='Testt', email='test@pytest.com', username='pytester', password='pytestpass', birthday='2000-01-01')
    return user

@pytest.fixture(scope='module')
def test_client():
    app = create_app()

    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens!