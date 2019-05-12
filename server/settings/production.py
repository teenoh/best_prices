import os
from .base import *

import django_heroku

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'best_prices',
        'USER': 'best_prices',
        'PASSWORD': 'best_prices123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# STATIC_ROOT = '/home/teenoh/webapps/best_prices_static/'

django_heroku.settings(locals())
