from woeclipse.models import User


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and is_admin are defined correctly
    """
    user = User(email='test@pytest.com', username='pytester', password='pytestpass')
    assert user.email == 'test@pytest.com'
    assert user.username == 'pytester'
    # assert user.password != 'pytestpass'
    assert not user.is_admin
    assert 1 == 1