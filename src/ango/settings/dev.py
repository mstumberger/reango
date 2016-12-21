from .base import *

SECRET_KEY = 'ojk@86z9*$zyuhge#3)p*%$q0psoo2lq*tv9jw90#1eezcl^y2'

# Must mention ALLOWED_HOSTS in production!
ALLOWED_HOSTS = ['*']

DEBUG = True

MIDDLEWARE.remove('django.middleware.csrf.CsrfViewMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(SRC_DIR, 'db.sqlite3'),
    }
}