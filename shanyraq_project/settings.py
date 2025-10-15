from pathlib import Path
import os
from dotenv import load_dotenv  # безопасная загрузка .env

# --- ЗАГРУЗКА ПЕРЕМЕННЫХ ИЗ .env ---
load_dotenv()

# --- БАЗОВЫЕ НАСТРОЙКИ ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- БЕЗОПАСНОСТЬ ---
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-local-key')

# ⚙️ На Vercel DEBUG должен быть False
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Разрешённые домены
ALLOWED_HOSTS = os.environ.get(
    'ALLOWED_HOSTS',
    '.vercel.app,127.0.0.1,localhost'
).split(',')

# --- ПРИЛОЖЕНИЯ ---
INSTALLED_APPS = [
    # Админ-дизайн
    'jazzmin',

    # Django system apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Твои приложения
    'articles',
    'users',
    'tests_app',
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # ✅ Добавляем WhiteNoise для статики (обязательно для Vercel)
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- URL / WSGI ---
ROOT_URLCONF = 'shanyraq_project.urls'
WSGI_APPLICATION = 'shanyraq_project.wsgi.application'

# --- БАЗА ДАННЫХ ---
# На Vercel — SQLite подходит для демонстрации, но лучше PostgreSQL через Supabase или Neon
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

# --- СТАТИКА И МЕДИА ---
STATIC_URL = '/static/'

# ⚙️ Настройка для Vercel: собранные файлы
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise — автоматическая компрессия и кеширование
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- JAZZMIN ---
JAZZMIN_SETTINGS = {
    "site_title": "Shanyraq Admin",
    "site_header": "Shanyraq Dashboard",
    "welcome_sign": "Добро пожаловать, Ризат!",
    "copyright": "© 2025 Shanyraq Journal",
}

# --- ПРОЧЕЕ ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
