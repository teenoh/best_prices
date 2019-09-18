import os
from .base import *

SECRET_KEY = 'secret'

ALLOWED_HOSTS = ['best-prices.us-west-2.elasticbeanstalk.com', 'develop.upcqqqxpap.us-west-2.elasticbeanstalk.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
    }
}