from pathlib import Path
import os
# .env dosyasını okumak için importlar
import dj_database_url
from dotenv import load_dotenv
print("BASE_DIR =", BASE_DIR)
print("STATICFILES_DIRS =", [os.path.join(BASE_DIR, 'static')])

BASE_DIR = Path(__file__).resolve().parent.parent

# .env dosyasını yükle
load_dotenv(os.path.join(BASE_DIR, '.env'))

# ==================================================
# === GÜVENLİK AYARLARI (.env'den okunur) ===
# ==================================================
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
# ==================================================


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    
    # Canlıya alma (Cloudinary & Whitenoise)
    'cloudinary_storage', 
    'django.contrib.staticfiles', 
    'cloudinary', 
    # 'whitenoise.runserver_nostatic' YANLIŞTI - BURADA OLMAMALI

    # Kendi Uygulamalarımız
    'products',
    'pages',
    'cart',
    'orders',
    'accounts',
    
    # 3. Parti Uygulamalar
    'crispy_forms',
    'crispy_bootstrap5',
    'django_filters',
    'anymail', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'auraluna_project.urls'

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
                'cart.context_processors.cart',
                'cart.context_processors.main_categories',
                'pages.context_processors.site_settings', 
                'cart.context_processors.structured_nav_categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'auraluna_project.wsgi.application'

# ==================================================
# === VERİTABANI AYARI (PostgreSQL/Neon) ===
# ==================================================
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}
# ==================================================


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_TZ = True

# ==================================================
# === STATİK VE MEDYA AYARLARI (Canlı) ===
# ==================================================
STATIC_URL = '/static/'
# Django'ya collectstatic için Orijinal dosyaların nerede olduğunu söyle:
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
# collectstatic'in dosyaları toplayacağı yer:
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Whitenoise depolaması:
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


# Cloudinary Medya ayarları:
CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL') 
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_STORAGE_MANAGE_STATICFILES = False # Statik dosyaları yönetme
MEDIA_URL = '/media/' 
# ==================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CART_SESSION_ID = 'cart'
LOGIN_REDIRECT_URL = "pages:home"
LOGOUT_REDIRECT_URL = "pages:home"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# ==================================================
# === E-POSTA (SMTP) VE STRIPE AYARLARI ===
# ==================================================
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS') == 'True'
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL') == 'True' 
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_API_VERSION = '2024-06-20'
# ==================================================
