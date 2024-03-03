import django.conf.locale
from django.conf import global_settings
import os
from src.settings.components.env import config
from tzlocal import get_localzone
from src.settings.components import PROJECT_PATH, BASE_DIR
from django.utils.translation import gettext_lazy as _

# from src.settings.components.redis import REDIS_HOST, REDIS_PORT

BASE_ENDPOINT = config('BASE_ENDPOINT', default='http://127.0.0.1:8000')
WS_ENDPOINT = config('WS_ENDPOINT', default='ws://127.0.0.1:8000')

# Application definition

DJANGO_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'rest_framework',
]
LOCAL_APPS = [
    "src.app",
    'src.accounts',
    'src.core',
    'src.blogs',
    'src.contact',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL = "accounts.User"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [PROJECT_PATH + "\\templates"],
        'DIRS': [os.path.join(PROJECT_PATH, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # "src.app.context_processors.vendor_files",
                "src.app.context_processors.menu_data",
                "src.app.context_processors.menu_items",
                "src.app.context_processors.language_ref",
            ],
        },
    },
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
print("CHECK LOCALE PATH BASE_DIR: ", os.path.join(BASE_DIR, 'locale'))

WSGI_APPLICATION = 'src.wsgi.application'
ASGI_APPLICATION = 'src.asgi.application'

# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [(REDIS_HOST, REDIS_PORT)],
#         },
#     },
# }

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR + 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/


def gettext_noop(s):
    return s


LANGUAGE_CODE = "en-us"
MODELTRANSLATION_LANGUAGES = ('en', 'ar', 'ckb')

LANGUAGES = [
    ('en', _('English')),
    ('ar', _('Arabic')),
    ("ckb", _("Kurdish")),
]


# Languages using BiDi (right-to-left) layout
LANGUAGES_BIDI = ["ar", "ckb"]

TIME_ZONE = str(get_localzone())

USE_I18N = True
USE_L10N = True

USE_TZ = True

# MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'  # Set your default language code
# MODELTRANSLATION_AUTO_POPULATE = True
# Set the language code to prepopulate
# MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'


# EXTRA_LANG_INFO = {
#     'ku': {
#         'bidi': True,  # right-to-left
#         'code': 'ku',
#         'name': 'Kurdish',
#     },
# }

# LANG_INFO = dict(django.conf.locale.LANG_INFO, **EXTRA_LANG_INFO)
# django.conf.locale.LANG_INFO = LANG_INFO




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
