from .base import *

SECRET_KEY = 'development'

DEBUG = True

TEMPLATE_DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
