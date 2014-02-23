"""
Django settings for nscwebsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from urllib.parse import urlparse

ON_OPENSHIFT=False
if 'OPENSHIFT_REPO_DIR' in os.environ:
    ON_OPENSHIFT=True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ucd0-1j%($*bj=)ym1zp535m4zq$(i$-4wsqq_5+7y5^)*)r+d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nscwebsite.urls'

WSGI_APPLICATION = 'nscwebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/
#databases
DATABASES={}
if 'OPENSHIFT_MYSQL_DB_URL' in os.environ:
    url=urlparse(os.environ.get('OPENSHIFT_MYSQL_DB_URL'))
    DATABASES['default']={
        'ENGINE':'django.db.backends.mysql',
        'NAME':os.environ['OPENSHIFT_APP_NAME'],
        'USER':url.username,
        'PASSWORD':url.password,
        'HOST':url.hostname,
        'PORT':url.port,
    }
else:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ZH_CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
if ON_OPENSHIFT:
    STATIC_ROOT = os.path.join(os.environ.get('OPENSHIFT_REPO_DIR'), 'wsgi', 'static')
else:
    STATIC_ROOT = os.path.join(BASE_DIR,'..','wsgi','static')

MEDIA_URL=STATIC_URL+'media/'

if 'OPENSHIFT_DATA_DIR' in os.environ:
    MEDIA_ROOT = os.environ.get('OPENSHIFT_DATA_DIR', 'media')
else:
    MEDIA_ROOT = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))

TEMPLATE_DIRS = (
     os.path.join(BASE_DIR,'templates'),
)


