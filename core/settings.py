from pathlib import Path
from django.contrib.messages import constants
import environ

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d+zn-yk(a#z&7^$(u(2e7dfeh(1%coz_=5rb%(f%jern)+3r%9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'crudveiculos.jnunesc.com.br', 'localhost']

CSRF_TRUSTED_ORIGINS = ['http://crudveiculos.jnunesc.com.br', 'https://jnunes-crudveiculos.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'app',
    'commons',
    'account',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

# A linha abaixo deve ser descomentada apenas quando debug=True para evitra o erro 500
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# A linha abaixo deve ser descomentada apenas quando o debug=False
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'resources/templates/'],
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

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': env('DJGDB_NAME'),
    #     'USER': env('DJGDB_USERNAME'),
    #     'PASSWORD': env('DJGDB_PASSWORD'),
    #     'HOST': env('DJGDB_HOST'),
    #     'PORT': env('DJGDB_PORT'),
    # }
}

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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Em produção, habilitar o statics STATIC_ROOT e desabilitar o STATICFILES_DIRS
# STATICFILES_DIRS = [BASE_DIR / 'resources/static/']
STATIC_ROOT = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Messages
MESSAGE_TAGS = {
    constants.ERROR: 'alert-danger',
    constants.WARNING: 'alert-warning',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-primary'
}

# Default URL settings
HOME_REDIRECT = '/veiculos/'
LOGIN_REDIRECT_URL = HOME_REDIRECT
LOGIN_URL = '/account/login/'
LOGOUT_REDIRECT_URL = '/account/login'

# SMTP Settings
EMAIL_HOST = env('DJGEMAIL_HOST')
EMAIL_PORT = env('DJGEMAIL_PORT')
EMAIL_HOST_USER = env('DJEMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('DJEMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
