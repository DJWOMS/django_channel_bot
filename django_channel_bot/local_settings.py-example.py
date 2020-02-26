import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lj0(t7h66%ebhzqberedfsf*svtwh_0r2pe)8&lc*hl'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nameDB',
        'USER': 'userDB',
        'PASSWORD': 'passDB',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

