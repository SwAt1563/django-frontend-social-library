from .base import *

ALLOWED_HOSTS = ['localhost', 'fronted-sl']

# Sqlite Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / '../db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, '../media')
STATIC_ROOT = os.path.join(BASE_DIR, '../static')

API_URL = 'http://backend-sl:6123'