import os

from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv("SC_DJANGO_HOST"),
        'PORT': os.getenv("SC_DJANGO_PORT"),
        'NAME': os.getenv("SC_DJANGO_NAME"),
        'USER': os.getenv("SC_DJANGO_USER"),
        'PASSWORD': os.getenv("SC_DJANGO_PASSWORD"),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

debug_mode = os.getenv("SC_DJANGO_DEBUG")
DEBUG = debug_mode.lower() == "true"

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
