from woeclipse.models import User
import pytest

@pytest.fixture(scope='module')
def new_user():
    user = User(first_name='Pie', last_name='Testt', email='test@pytest.com', username='pytester', password='pytestpass', birthday='2000-01-01')
    return user

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and is_admin are defined correctly
    """
    user = User(first_name='Pie', last_name='Testt', email='test@pytest.com', username='pytester', password='pytestpass', birthday='2000-01-01')
    assert user.first_name == 'Pie'
    assert user.last_name == 'Testt'
    assert user.email == 'test@pytest.com'
    assert user.username == 'pytester'
    assert user.password == 'pytestpass'
    assert user.birthday == '2000-01-01'

def test_new_user_fixture(new_user):
    assert new_user.last_name == 'Testt'