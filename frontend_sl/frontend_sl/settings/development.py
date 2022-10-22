from .base import *


# Sqlite Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / '../db.sqlite3',
    }
}


API_URL = 'http://backend-sl:6123'