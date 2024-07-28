from pathlib import Path
# from decouple import config
import os

""" VAR ----------------------------------------------------------------------------------------"""
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '367102371209387090218390128301283012'
ROOT_URLCONF = 'core.urls'
LOGOUT_REDIRECT_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/cross-auth/'
AUTH_USER_MODEL = 'accounts.User'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

SERVER = 'local'
DEBUG = True

if SERVER == 'server':
    SITE_ID = 1
    DOMAIN_URL = 'yourdomain.com/'
    STRIPE_PUBLISHABLE_KEY = 'pk_test_51KNUx8GWh1G1v77h4cAKDbEvH3wEbK4yVZfSGKT5f5wgShK8cipV0ctpNrZ2tqt63fsVmJp4sAk6cs8mogGlzHlL00CTKGtGvE'
    STRIPE_SECRET_KEY = 'sk_test_51KNUx8GWh1G1v77hDR40VBVDDZTK2pgUZMk0yxDyN4evl4lBg2LyxFyOQCDoLQWhgy1t9bAzcC63c681rUe5mxtv00vHfKyh2r'

    ALLOWED_HOSTS = ['yourdomain.com']
    GOOGLE_CALLBACK_ADDRESS = "https://redsparrow.exarth.com/accounts/google/login/callback/"
else:
    SITE_ID = 1
    DOMAIN_URL = 'http://127.0.0.1:8000/'
    GOOGLE_CALLBACK_ADDRESS = "http://127.0.0.1:8000/accounts/google/login/callback/"
    ALLOWED_HOSTS = ['*']

    STRIPE_PUBLISHABLE_KEY = 'pk_test_51KNUx8GWh1G1v77h4cAKDbEvH3wEbK4yVZfSGKT5f5wgShK8cipV0ctpNrZ2tqt63fsVmJp4sAk6cs8mogGlzHlL00CTKGtGvE'
    STRIPE_SECRET_KEY = 'sk_test_51KNUx8GWh1G1v77hDR40VBVDDZTK2pgUZMk0yxDyN4evl4lBg2LyxFyOQCDoLQWhgy1t9bAzcC63c681rUe5mxtv00vHfKyh2r'

""" APPS ---------------------------------------------------------------------------------------"""
INSTALLED_APPS = [
    # 'src.admins.apps.AppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

    # REQUIRED_APPLICATIONS
    "crispy_forms",
    "crispy_bootstrap4",
    'django_filters',
    'phonenumber_field',

    'rest_framework',
    'rest_framework.authtoken',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # CUSTOM APPS
    'src.website',
    'src.accounts',
    'src.api',

    'src.admins',
    'src.staff',
    'src.customer',
    'src.payments',

    # MUST BE AT THE END
    'notifications'

]

""" MIDDLE WARES ----------------------------------------------------------------------------"""
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

""" TEMPLATES -------------------------------------------------------------------------------"""
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
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

""" DATABASES ------------------------------------------------------------------------------------"""

if SERVER != 'deploy':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

""" VALIDATORS -----------------------------------------------------------------------------------"""

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

""" INTERNATIONALIZATION -------------------------------------------------------------------------"""

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_L10N = True
USE_TZ = True

""" STATIC AND MEDIA ----------------------------------------------------------------------------"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'donald.duck0762@gmail.com'
EMAIL_HOST_PASSWORD = 'mghulhfjugnqwuoz'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'Support-Team <donald.duck0762@gmail.com>'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
STATIC_ROOT = BASE_DIR / 'assets'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# EMAIL_HOST = 'smtp.office365.com'
# EMAIL_HOST_USER = 'theRed Sparrow01@gmail.com'
# EMAIL_HOST_PASSWORD = 'poiu098765'
# SERVER_EMAIL = EMAIL_HOST_USER
# EMAIL_PORT = 587
# EMAIL_USE_SSL = False
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'Support-Team <support@Red Sparrowmentpro.com>'

""" RESIZER IMAGE --------------------------------------------------------------------------------"""
DJANGORESIZED_DEFAULT_SIZE = [1920, 1080]
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {
    'JPEG': ".jpg",
    'PNG': ".png",
    'GIF': ".gif"
}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True

""" ALL-AUTH SETUP --------------------------------------------------------------------------------"""

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

ACCOUNT_LOGOUT_ON_GET = True
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_EMAIL_VERIFICATION = 'none'

# Make sure to remove this in live server - use it on local server
# if SERVER != 'server':
#     INSTALLED_APPS += [
#         'django_browser_reload'
#     ]
#     MIDDLEWARE += [
#         'django_browser_reload.middleware.BrowserReloadMiddleware'
#     ]
