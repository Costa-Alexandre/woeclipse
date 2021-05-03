from flask import current_app
import random, os, string

AVATAR_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Checks if an extension is valid
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in AVATAR_ALLOWED_EXTENSIONS

def get_random_avatar():
    path = current_app.config['RANDOM_AVATAR_PATH']
    avatar_list = os.listdir(path)
    filename = avatar_list[random.randrange(len(avatar_list))]
    return filename

def generate_filename(ext):
    filename = "".join(random.choices(string.ascii_lowercase, k=16)) + "." + ext
    return filename

def get_extention(avatar):
    extension = avatar.filename.rsplit('.', 1)[1].lower()
    return extension