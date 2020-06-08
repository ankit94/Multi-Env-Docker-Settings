from .base import *

# Test settings
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = False

# Set the Cache
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': ''
#     }
# }
#
# # Set password hasher to speedup tests
# # PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher', ]
#
# # Store django templates in memory
# TEMPLATES[0]['OPTIONS']['loaders'] = [
#     ['django.template.loaders.cached.Loader', [
#         'django.template.loaders.filesystem.Loader',
#         'django.template.loaders.app_directories.Loader', ]
#         , ]
#     , ]
