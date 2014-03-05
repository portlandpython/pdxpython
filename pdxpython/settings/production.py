from .base import *

SECRET_KEY = get_environment_variable('SECRET_KEY')

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_environment_variable('DATABASES_DEFAULT_NAME'),
        'USER': get_environment_variable('DATABASES_DEFAULT_USER'),
        'PASSWORD': get_environment_variable('DATABASES_DEFAULT_PASSWORD'),
    }
}
