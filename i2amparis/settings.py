"""
Django settings for i2amparis project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os, sys
import dj_database_url

# from i2amparis.private_settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


CORS_ORIGIN_ALLOW_ALL = True

X_FRAME_OPTIONS = 'SAMEORIGIN'

ALLOWED_HOSTS = ['*']

# DJANGO-CACHALOT SETTINGS


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cachalot',
    'visualiser',
    'feedback_form',
    'i2amparis_main',
    'harmonisation_map_tool',
    'data_manager'
]


# Cachalot configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'i2amparis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'i2amparis.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_FINDER = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),

]

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com'
EMAIL_PORT = 587
EMAIL_PROTOCOL = 'smtp'
EMAIL_HOST_USER = 'noreply@epu.ntua.gr'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply@epu.ntua.gr'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")
EMAIL_FROM = 'noreply@epu.ntua.gr'
SERVER_EMAIL = 'noreply@epu.ntua.gr'

GOOGLE_RECAPTCHA_SITE_KEY =  os.environ.get("GOOGLE_RECAPTCHA_SITE_KEY")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# PRIVATE SETTINGS

# APP SETTINGS
SECRET_KEY = os.environ.get("SECRET_KEY", "test_key")
DEBUG = int(os.environ.get("DEBUG", default=1))

# CAPTCHA SETTINGS
GOOGLE_RECAPTCHA_SECRET_KEY = os.environ.get("GOOGLE_RECAPTCHA_SECRET_KEY")

# EMAIL SETTINGS
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

#DATABASE SETTINGS
DATABASES = {
    'default': {
    }
}
if "DATABASE_URL" in os.environ:
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)
else:
    sys.path.append(os.path.abspath(os.path.join(BASE_DIR,".secrets")))
    from secret_config import db_dev_config

    DATABASES['default'].update(db_dev_config)

