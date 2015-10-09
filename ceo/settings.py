"""
Django settings for ceo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

try:
    from ceo.deploy_settings import *
except:
    from ceo.local_settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = LOCAL_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = LOCAL_DEBUG

TEMPLATE_DEBUG = LOCAL_TEMPLATE_DEBUG

ALLOWED_HOSTS = LOCAL_ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = (
    'flat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taggit',
    'cms',
    'schedule',
    'upload',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ceo.urls'

WSGI_APPLICATION = 'ceo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = LOCAL_DATABASES

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = LOCAL_STATIC_ROOT

STATIC_URL = LOCAL_STATIC_URL

MEDIA_ROOT = LOCAL_MEDIA_ROOT

MEDIA_URL = LOCAL_MEDIA_URL

STATICFILES_DIRS = (
    BASE_DIR + '/ceo/static/',
)

TEMPLATE_DIRS = (
    BASE_DIR + '/ceo/templates/',
    BASE_DIR + '/cms/templates/',
    BASE_DIR + '/events/templates/',
)

APPEND_SLASH = True

DJANGO_WYSIWYG_FLAVOR = 'tinymce_advanced'
