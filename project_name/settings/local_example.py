# dev settings

from {{ project_name }}.settings.base import *

# SECRET KEY: generate a secret key to use with the application
# http://www.miniwebtool.com/django-secret-key-generator/

SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
INTERNAL_IPS = ('127.0.0.1',)

# STATIC_ROOT is required as of Django 1.6.2
# This should be a real apache served location if you're using Apache.
STATIC_ROOT = '/tmp/'

# django compressor and less-c compiler

COMPRESS_OFFLINE = False
COMPRESS_ENABLED = False
