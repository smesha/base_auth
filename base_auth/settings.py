from dotenv import load_dotenv
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

DEBUG = bool(os.environ['DEBUG'])

SECRET_KEY = os.environ['SECRET_KEY']


# Для коректного получения списка ALLOWED_HOSTS он должен иметь следующий вид: host1,host2,host3
_allowed_hosts = os.environ['ALLOWED_HOSTS'] 
ALLOWED_HOSTS = _allowed_hosts.split(',') if _allowed_hosts != '' else []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    "users",
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

ROOT_URLCONF = 'base_auth.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'base_auth.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': os.environ['DATABASE_ENGINE'],
        'NAME': BASE_DIR / os.environ['DATABASE_NAME'],
    }
}

      
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


LANGUAGE_CODE = os.environ['LANGUAGE_CODE']

TIME_ZONE = os.environ['TIME_ZONE']

USE_I18N = True

USE_TZ = True


STATIC_URL = os.environ['STATIC_URL']


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


USERS = {
    "templates": {
        'signin': 'auth/signin.html',
        'signup': 'auth/signup.html',
        'logout': 'auth/logout.html',
        'confirm_logout': 'auth/confirm_logout.html',
        'password_reset': 'auth/password_reset.html',
        'password_reset_done': 'auth/password_reset_done.html',
    }
}

LOGIN_URL = 'users:signin'
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = 'users:logout'

EMAIL_BACKEND = os.environ['EMAIL_HOST_BACKEND']
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']
EMAIL_USE_TLS = True
