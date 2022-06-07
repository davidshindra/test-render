from .settings import *

SECRET_KEY = 'keep me safe :)'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testrender',
        'USER': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': 5432
    }
}