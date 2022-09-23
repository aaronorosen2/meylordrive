"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 2.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from rest_framework.settings import api_settings
from datetime import timedelta
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSRF_TRUSTED_ORIGINS = ['https://mapi.dreampotential.org']



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z@g8x(zh990d)ti@6)^a7ng2=t21_)dkwfs4n50d#(v@dy@f=r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',
    'agent',
    'rest_framework',
    'django_rest_passwordreset',
    'knox',
    'corsheaders',
    'usersystem',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',

]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = False
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'web.urls'

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

WSGI_APPLICATION = 'web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

db_password = os.environ.get('db_password', 'EhB4bINnDFmzI0Bg')
db_user = os.environ.get('db_user', 'postgres')
db_host = os.environ.get('db_user', '3.21.231.89')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': db_user,
        'HOST': db_host,
        'PORT': '5775',
        'PASSWORD': db_password,
    }
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


# Make knox’s Token Authentication default
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication', ),
}

# KNOX
REST_KNOX = {
    'USER_SERIALIZER': 'usersystem.serializer.UserSerializer',
}


REST_KNOX = {
    'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
    'AUTH_TOKEN_CHARACTER_LENGTH': 64,
    'TOKEN_TTL': timedelta(hours=10),
    'USER_SERIALIZER': 'knox.serializers.UserSerializer',
    'TOKEN_LIMIT_PER_USER': None,
    'AUTO_REFRESH': False,
    #   'EXPIRY_DATETIME_FORMAT': api_settings.DATETME_FORMAT,
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = 'AKIARWLPGYIKRQXN5VXR'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'sfappv2'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

ALLOWED_HOSTS = ['*']

# Email
EMAIL_BACKEND = 'django_ses.SESBackend'
EMAIL_AWS_ACCESS_KEY_ID = 'AKIARWLPGYIKWTF4OEPZ'
EMAIL_AWS_SECRET_ACCESS_KEY = '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'
DEFAULT_FROM_EMAIL = 'mail-api@dreampotential.org'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

APPEND_SLASH = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
