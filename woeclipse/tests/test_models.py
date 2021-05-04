from woeclipse.models import load_user
from woeclipse.website import db


def test_new_user_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and is_admin are defined correctly
    """
    assert new_user.first_name == 'Pie'
    assert new_user.last_name == 'Testt'
    assert new_user.email == 'test@pytest.com'
    assert new_user.username == 'pytester'
    assert new_user.password == 'pytestpass'
    assert new_user.birthday == '2000-01-01'
    assert new_user.id == 999
    assert str(new_user) == '<User pytester>'


def test_new_event(new_event):
    assert new_event.date == '2000-01-01'
    assert new_event.description == 'This is an event'
    assert new_event.event_name == 'Tournment 2021'
    assert str(new_event) == '<Event Tournment 2021>'


def test_participant(new_event, new_user):
    new_event.users.append(new_user)

    assert new_user in new_event.users
    assert new_event.users[0].username == 'pytester'


def test_load_user(app, new_user):
    db.session.add(new_user)
    assert load_user(999).id == 999
