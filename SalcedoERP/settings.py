# coding=utf-8

"""
Django settings for SalcedoERP project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, se e
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

import locale

#locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
# locale.currency(1000, grouping=True)
# español para windows
#locale.setlocale(locale.LC_ALL, "")
# español para linux
#locale.setlocale(locale.LC_ALL, "es_MX.UTF-8")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9+ue&u-t+v6s8_^7ivxbxfec%pszd8rhxm%0_$@*#$j2@a_6$$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

#LANGUAGE_CODE = 'es'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'smart_selects',
    'oauth2_provider',
    'users',
    'SharedCatalogs',
    'ERP',
    'reporting',
    'DataUpload',
    'HumanResources',
    'Assistance',
    'Accounting',
    'multiselectfield',
    'tinymce',
'django.contrib.humanize',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SalcedoERP.urls'
TEMPLATETAGS_DIRS = (
    os.path.join(BASE_DIR, 'users/templatetags/'),
    os.path.join(BASE_DIR, 'HumanResources/templatetags/'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'SalcedoERP.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': 'SalcedoERP/my.cnf',
        },
        'ATOMIC_REQUESTS': True
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'ERP/media')
MEDIA_URL = "/media/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


import sys
reload(sys)
sys.setdefaultencoding('utf-8')



PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join('static')
# STATICFILES_DIRS = [
#      os.path.join(BASE_DIR, "static"),
# ]

STATIC_FILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
USE_L10N = True
#USE_THOUSAND_SEPARATOR = True
print os.path.join(PROJECT_ROOT, '../static')
# Loading local settings to the project.
try:
    from .local_settings import *
except ImportError as e:
    pass
