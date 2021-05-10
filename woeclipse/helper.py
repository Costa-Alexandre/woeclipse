import random
import os
import string
from flask import current_app

AVATAR_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# Checks if an extension is valid
def allowed_file(filename):
    """ Given a filename, splits the string to get the file's extension
    and returns true if that extension belongs to a list
    AVATAR_ALLOWED_EXTENSION containing allowed extensions (e.g. 'jpg').
    """
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in AVATAR_ALLOWED_EXTENSIONS


def get_random_avatar():
    """ Selects randomly one file from the RANDOM_AVATAR_PATH, specified
    at config.py, and returns this file's name.
    """
    path = current_app.config['RANDOM_AVATAR_PATH']
    avatar_list = os.listdir(path)
    filename = avatar_list[random.randrange(len(avatar_list))]
    return filename


def generate_filename(ext):
    fname = "".join(random.choices(string.ascii_lowercase, k=16)) + "." + ext
    return fname


def get_extension(avatar):
    extension = avatar.filename.rsplit('.', 1)[1].lower()
    return extension

def rank_users(users):
    """ given a list of users, return the same list sorted by the points_system
    set as method for a user in models.py, with an additional list for points
    """
    users_rank = []
    sorted_users = []
    for user in users:
        user_stats = [user, user.points()]
        users_rank.append(user_stats)
    
    users_rank.sort(key=lambda i: i[1], reverse=True)
    
    for user_stats in users_rank:
        sorted_users.append(user_stats[0])
    return sorted_users

def user_rank(user, users):
    sorted_users = rank_users(users)
    rank = sorted_users.index(user) + 1
    return rank
