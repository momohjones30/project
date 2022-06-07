import django_heroku
# from decouple import project
import os

from.base import *

# SECRET_KEY = project('SECRET_KEY')
with open(os.path.join(BASE_DIR, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'friendswood.herokuapp.com']
