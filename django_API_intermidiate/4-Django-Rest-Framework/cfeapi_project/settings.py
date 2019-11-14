"""
Django settings for cfeapi_project project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '19#v_e(ha_zr1f(&pi$1yr+vbx2g%hio*_4cyt^762#al=g$io'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# APPEND_SLASH = False     # || Dafault value = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    ### 3rd Party Application ###
    ###### Django-Rest-Framework ###
    'rest_framework',

    ### My created apps ###
    'accounts',
    'updates',
    'status',
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

ROOT_URLCONF = 'cfeapi_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'cfeapi_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },

    # ORACLE Database Configuration
    # 'default': {
    #     'ENGINE': 'django.db.backends.oracle',
    #     #'mode': 'oracle.SYSDBA',
    #     'NAME': 'testpdb',
    #     'USER': 'SHIFULLAH',
    #     'PASSWORD': 'shifullah',
    #     'HOST': '10.11.201.55',
    #     'PORT': '1525',
    # },
    # 'default': {
    #     'ENGINE':   'django.db.backends.oracle',
    #     'NAME':     '10.11.201.55:1525/testpdb',
    #     'USER':     'SHIFULLAH',
    #     'PASSWORD': 'shifullah',
    # },

    # # # POSTGRE SQL Database Configuration
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'emp_dept_table',
    #     'USER': 'postgres',
    #     'PASSWORD': 'postgres1234',
    #     'HOST': '127.0.0.1',
    #     'PORT': '5432',
    # },

    # MYSQL Database
    # 'default': {
    #     'NAME': 'user_data',
    #     'ENGINE': 'mysql.connector.django',
    #     'USER': 'mysql_user',
    #     'PASSWORD': 'password',
    #     'OPTIONS': {
    #       'autocommit': True,
    #     },
    # }

}


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

STATIC_URL = '/static/'

# Own MEDIA FILES 
MEDIA_ROOT      = os.path.join(BASE_DIR, 'static-server', 'media-root') # os.path.dirname(BASE_DIR)
MEDIA_URL       = '/media/'

# Imported everything form my customize configuration folder --> "restconfig"
from cfeapi_project.restconf.main import *


