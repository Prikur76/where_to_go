from pathlib import Path
from environs import Env

from .base import *


env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.list('SECRET_KEY', 'REPLACE ME!')

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
