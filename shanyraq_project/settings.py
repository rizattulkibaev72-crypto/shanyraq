# shanyraq_project/settings.py
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'change-me-in-production')
DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1', 'localhost',
    'rizat.pythonanywhere.com',         # ← твой домен на PA
]
CSRF_TRUSTED_ORIGINS = [
    'https://rizat.pythonanywhere.com',
]

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes',
    'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles',
    'articles', 'users', 'tests_app',
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # обязательно для статики
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- ШАБЛОНЫ (TEMPLATES) ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # путь к твоей папке templates
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

ROOT_URLCONF = 'shanyraq_project.urls'
WSGI_APPLICATION = 'shanyraq_project.wsgi.application'

# SQLite ок на старт. (Если потом пойдёшь в Postgres — поменяем)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME'  : BASE_DIR / 'db.sqlite3',
    }
}

# --- ВАЛИДАЦИЯ ПАРОЛЕЙ ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- ЛОКАЛИЗАЦИЯ ---
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_TZ = True

# Статика/медиа для PA
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']           # если у тебя есть /Django/static
STATIC_ROOT = BASE_DIR / 'staticfiles'             # сюда PA будет собирать

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- JAZZMIN ---
JAZZMIN_SETTINGS = {
    "site_title": "Shanyraq Admin",
    "site_header": "Shanyraq Dashboard",
    "welcome_sign": "Добро пожаловать, Ризат!",
    "copyright": "© 2025 Shanyraq Journal",
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
