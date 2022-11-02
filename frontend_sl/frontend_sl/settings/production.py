from .base import *

ALLOWED_HOSTS = ['localhost', 'fronted-sl'] + list(os.environ.get("DJANGO_ALLOWED_HOSTS").split(" "))

#CSRF


# for security

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_TRUSTED_ORIGINS = ['https://*.social-library-1563.ml']  # to support https domains
SECURE_SSL_REDIRECT = True  # http redirect to https
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
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



#CROS
CORS_ALLOW_CREDENTIALS = False

CORS_ALLOWED_ORIGINS = [
    'https://social-library-1563.ml',
    'https://www.social-library-1563.ml',
    'localhost',
    '127.0.0.1',
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]