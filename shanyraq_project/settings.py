"""
Django settings for shanyraq_project project.
Adapted for Render deployment by Rizat Tulkibayev.
"""

from pathlib import Path
import os

# --- БАЗОВЫЕ НАСТРОЙКИ ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- БЕЗОПАСНОСТЬ ---
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-local-key')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Основные домены
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# --- ПРИЛОЖЕНИЯ ---
INSTALLED_APPS = [
    # Интерфейс администратора
    'jazzmin',

    # Стандартные приложения Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Ваши приложения
    'articles',
    'users',
    'tests_app',
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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
# На Render можно начать с SQLite (для теста),
# позже перейти на PostgreSQL при необходимости
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
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

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

# --- РЕНДЕР / ПРОДАКШН ЛОГИКА ---
# Render автоматически создаёт переменную окружения RENDER,
# по ней отключаем DEBUG и добавляем домен
if os.environ.get('RENDER', None):
    DEBUG = False
    ALLOWED_HOSTS.append('shanyraq.onrender.com')

# Логирование (по желанию)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
