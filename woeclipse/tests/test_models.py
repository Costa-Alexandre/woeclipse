
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

def test_new_event(new_event):
    assert new_event.date == '2000-01-01'
    assert new_event.description == 'This is an event'
    assert new_event.event_name == 'Tournment 2021'
