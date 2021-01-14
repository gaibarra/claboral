from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'contrato',
         'HOST': 'localhost',
         'USER': 'postgres',
         'PASSWORD': '6Vlgpcr/zaira',
         'PORT': 5432
     }
 }

# import dj_database_url
# from decouple import config


# DATABASES = {
#     'default': dj_database_url.config(
#         default=config('DATABASE_URL')
#     )

# }