"""
Django settings for core project.
"""

import re
import socket
from datetime import timedelta
from pathlib import Path
from decouple import Csv, config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# apps/
APPS_DIR = BASE_DIR / 'apps'
# core
CORE_DIR = BASE_DIR / 'core'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-c(km)ivwjya95662#a(fv(8@r1i$pkz4lfqtu_ps66n4nf0eq6')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# # USER INFO
# ADMIN_USERNAME = config("ADMIN_USERNAME")
# ADMIN_EMAIL = config("ADMIN_EMAIL")

# ADMINS = ((ADMIN_USERNAME, ADMIN_EMAIL),)


# MANAGERS = ADMINS

ADMIN_URL = 'admin/'

SITE_ID = 1

ANONYMOUS_USER_ID = 0

DEBUG_PROPAGATE_EXCEPTIONS = True

INTERNAL_IPS = ["127.0.0.1"]

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1,localhost", cast=Csv())

AUTHENTICATION_BACKENDS = [
    # "axes.backends.AxesStandaloneBackend", # enhanced to include rate limit on authenitation
    # "apps.authentication.auth_backend.EmailOrUsernameAuthBackend", # not yet implemented
    "django.contrib.auth.backends.ModelBackend",
]

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework_simplejwt', # for json web token authentications
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders', #
    'djoser', # TODO: SOCIAL AUTH CONFIG
    'phonenumber_field', # correct country code for db storages
    'notifications',
    'storages',
    'imagekit', # process images before uploads e.g set size and quality
    'django_cleanup', # prevent duplication of files in files fields
    'drf_spectacular', # For api documentation in development
    'drf_spectacular_sidecar', # provides static files for offline view of api documentation
]

LOCAL_APPS = [
    'apps.authentication',
    'apps.creators',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL = 'authentication.User'

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

CORS_ALLOWED_ORIGINS = (
    # TODO - set this properly for production
    "http://localhost:8000",
    "http://localhost:3000", # should correspond to fronted server in development
    "http://localhost:5173",
)

CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# By Default swagger ui is available only to admin user(s). You can change permission classes to change that
# See more configuration options at https://drf-spectacular.readthedocs.io/en/latest/settings.html#settings
SPECTACULAR_SETTINGS = {
    "TITLE": "AfroPix backend API",
    "DESCRIPTION": "Documentation of API endpoints of AfroPix backed",
    "VERSION": "1.0.0",
    "COMPONENT_SPLIT_REQUEST": True,
    "ENUM_ADD_EXPLICIT_BLANK_NULL_CHOICE": True,
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
    "SWAGGER_UI_DIST": "SIDECAR",  # shorthand to use the sidecar instead
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}

DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "auth/password/reset/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "auth/username/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "auth/account/activate/{uid}/{token}",
    "INVITE_ACTIVATION_URL": "auth/account/activate/invite/{uid}/{token}",
    "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND": True,
    "SEND_ACTIVATION_EMAIL": False,
    "SEND_CONFIRMATION_EMAIL": True,
    "HIDE_USERS": True,
    "SERIALIZERS": {
        # "user": "apps.users.api.serializers.UserSerializer",
        # "current_user": "apps.users.api.serializers.UserSerializer",
    },
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "UPDATE_LAST_LOGIN": True,
}

PHONENUMBER_DB_FORMAT = "INTERNATIONAL"
PHONENUMBER_DEFAULT_REGION = "KE"
PHONENUMBER_DEFAULT_FORMAT = "INTERNATIONAL"


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "axes.middleware.AxesMiddleware", # TODO: uncomment when ratelimit is enabled with django axes
]

ROOT_URLCONF = "core.urls"

SESSION_EXPIRE_AT_BROWER_CLOSE = True

SESSION_SAVE_EVERY_REQUEST = True

SESSION_COOKIE_AGE = 60 * 30

CSRF_COOKIE_NAME = "XSRF-TOKEN"

CSRF_HEADER_NAME = "HTTP_X_XSRF_TOKEN"

ROOT_URLCONF = "core.urls"

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

X_FRAME_OPTIONS = "SAMEORIGIN"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ CORE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# IGNORE 404 FROM SITES REQUESTING CGI, PHP AND WEB CRAWLERS
IGNORABLE_404_URLS = [
    re.compile(r"\.(php|cgi)$"),
    re.compile(r"^/phpmyadmin/"),
    re.compile(r"^/apple-touch-icon*\.png$"),
    re.compile(r"^/favicon\.ico$"),
    re.compile(r"^/robots\.txt$"),
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = config("LANGUAGE_CODE", default="en-us")

TIME_ZONE = config("TIME_ZONE", default="UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [CORE_DIR / "locale"]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
STATIC_ROOT = CORE_DIR / "static"
# STATICFILES_DIRS = [CORE_DIR / "static"]
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media" # for development purposes, not tracked by git

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}


RUN_MODE = config("RUN_MODE", default="development")

# production settings
if RUN_MODE == "production":
    # ==============================================================================
    # EMAIL CONFIGURATIONS
    # ===============================================================================
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST_ADDR = config("EMAIL_HOST")
    EMAIL_HOST = socket.gethostbyname(EMAIL_HOST_ADDR)  # Speed up sending emails
    EMAIL_PORT = config("EMAIL_PORT")
    EMAIL_HOST_USER = config("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    EMAIL_USE_SSL = True

    # ==============================================================================
    # SECURITY CONFIGURATIONS
    # ==============================================================================

    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True

    SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_SSL_REDIRECT = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')

    SESSION_COOKIE_SECURE = True

# local settings
else:
    # send emails to console
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = config("EMAIL_HOST_USER", default='noreply@afropix.com')
