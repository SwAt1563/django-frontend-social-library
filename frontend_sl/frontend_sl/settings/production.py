from .base import *

ALLOWED_HOSTS = ['localhost', 'fronted-sl'] + list(os.environ.get("DJANGO_ALLOWED_HOSTS").split(" "))

#CSRF
# to support https domains
CSRF_TRUSTED_ORIGINS = ['https://*.social-library-1563.ml']

# Database


# Postgresql Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),

    }
}
# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, '../mediafiles')
STATIC_ROOT = os.path.join(BASE_DIR, '../staticfiles')

API_URL = 'https://social-library-api-1563.ml'