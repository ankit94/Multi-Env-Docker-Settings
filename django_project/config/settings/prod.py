from .base import *

ADMIN_URL = env('DJANGO_ADMIN_URL')
# INSTALLED_APPS += ['gunicorn', ]
DEBUG = True
# Add your domain to:
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['127.0.0.1', ])
print(DEBUG, ALLOWED_HOSTS)
