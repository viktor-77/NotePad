import os

from dotenv import load_dotenv

from .base import *

load_dotenv(BASE_DIR / ".env")

# Debug
DEBUG = True

# SECURITY WARNING
SECRET_KEY = os.getenv("SECRET_KEY", "django_insecure_key_...")

# Debug‑toolbar
INTERNAL_IPS = ["127.0.0.1"]
INSTALLED_APPS.insert(0, "debug_toolbar")
MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")

# Static files
STATICFILES_DIRS = [BASE_DIR / "static"]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
