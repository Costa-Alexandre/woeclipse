from woeclipse.helper import allowed_file, generate_filename,\
    get_extension, get_random_avatar
from woeclipse.models import Avatar


def test_allowed_file():
    # Test allowed extensions
    assert allowed_file('img.png')
    assert allowed_file('img.gif')
    assert allowed_file('img.jpeg')
    assert allowed_file('img.jpg')
    assert not allowed_file('img.png.doc')
    assert not allowed_file('img.pdf')
    assert not allowed_file('img.doc')
    assert not allowed_file('img.xml')
    assert not allowed_file('')
    assert not allowed_file('png.pdf')
    assert not allowed_file('png')


def test_generate_filename():
    # function expects a random 16-letter string name concatenated with
    # a extension (e.g. 'abcdefghijklmnop.png')
    assert len(generate_filename(ext='png')) > 16
    assert type(generate_filename('png')) == str
    assert generate_filename('png') != generate_filename('png')
    assert generate_filename('png')[-3:] == 'png'
    assert generate_filename('png')[-4:] == '.png'


def test_get_extension(avatar):
    # Given a avatar object with 'random.png' attribute, get extension
    assert get_extension(avatar) == 'png'
    assert get_extension(avatar) != 'jpg'


def test_get_random_avatar(app):
    assert type(get_random_avatar()) == str


def test_all_helper_functions(app):
    assert allowed_file(
        generate_filename(
            get_extension(
                Avatar(
                    filename=get_random_avatar()
                )
            )
        )
    )
