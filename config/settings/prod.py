import os

from django.core.exceptions import ImproperlyConfigured

from dotenv import load_dotenv

from .base import *

load_dotenv(BASE_DIR / ".env")

# DEBUG
DEBUG = False

# SECURITY WARNING
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

ALLOWED_HOSTS.append("instaload-sl70.onrender.com")

SECRET_KEY = os.getenv("SECRET_KEY", "django_insecure_key_...")
# SECRET_KEY = os.getenv("SECRET_KEY")
# if not SECRET_KEY:
#     raise ImproperlyConfigured("SECRET_KEY must be set in environment")

# Whitenoise middleware
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# Database
required_db_env = (
    "POSTGRES_DB", "POSTGRES_USER", "POSTGRES_PASSWORD", "POSTGRES_HOST"
)

for env in required_db_env:
    if not os.getenv(env):
        raise ImproperlyConfigured("Missing database env vars")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': int(os.environ.get('POSTGRES_PORT', 5432)),
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}

# Security settings
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
