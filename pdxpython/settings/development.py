from .base import *

SECRET_KEY = 'development'

DEBUG = True

TEMPLATE_DEBUG = True

ENV_FILE = os.path.join(BASE_DIR, '../development.env')

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
    'django_env_server'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
