"""
Django settings for care_a_bit project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'frel&33-^yd!7=5j6etma$*+y*qmyogzc-g$16qx&vaudcy1^c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'donor',
    'ngo',
    'cities_light',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'care_a_bit.urls'

WSGI_APPLICATION = 'care_a_bit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'HOST': 'http://localhost:8000',
        'PORT': '5432'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/deployment/
STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (STATIC_PATH,)

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = ( TEMPLATE_PATH,)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REQUIRED_ADDRESS_FIELDS = (
    'first_name', 'last_name', 'line1', 'line4', 'postcode', 'country')
# ALLOW_ANON_REVIEWS = False
MISSING_IMAGE_URL = 'image_not_found.jpg'

HOSTNAME = 'http://127.0.0.1:8000'

SERVER_EMAIL = 'shubug7320@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'shubug7320@gmail.com'
EMAIL_HOST_PASSWORD = 'creatordumping'


POSTCODES_REGEX = {
    'AC': r'^[A-Z]{4}[0-9][A-Z]$',
    'AD': r'^AD[0-9]{3}$',
    'AF': r'^[0-9]{4}$',
    'AI': r'^AI-2640$',
    'AL': r'^[0-9]{4}$',
    'AM': r'^[0-9]{4}$',
    'AR': r'^([0-9]{4}|[A-Z][0-9]{4}[A-Z]{3})$',
    'AS': r'^[0-9]{5}(-[0-9]{4}|-[0-9]{6})?$',
    'AT': r'^[0-9]{4}$',
    'AU': r'^[0-9]{4}$',
    'AX': r'^[0-9]{5}$',
    'AZ': r'^AZ[0-9]{4}$',
    'BA': r'^[0-9]{5}$',
    'BB': r'^BB[0-9]{5}$',
    'BD': r'^[0-9]{4}$',
    'BE': r'^[0-9]{4}$',
    'BG': r'^[0-9]{4}$',
    'BH': r'^[0-9]{3,4}$',
    'BL': r'^[0-9]{5}$',
    'BM': r'^[A-Z]{2}([0-9]{2}|[A-Z]{2})',
    'BN': r'^[A-Z}{2}[0-9]]{4}$',
    'BO': r'^[0-9]{4}$',
    'BR': r'^[0-9]{5}(-[0-9]{3})?$',
    'BT': r'^[0-9]{3}$',
    'BY': r'^[0-9]{6}$',
    'CA': r'^[A-Z][0-9][A-Z][0-9][A-Z][0-9]$',
    'CC': r'^[0-9]{4}$',
    'CH': r'^[0-9]{4}$',
    'CL': r'^([0-9]{7}|[0-9]{3}-[0-9]{4})$',
    'CN': r'^[0-9]{6}$',
    'CO': r'^[0-9]{6}$',
    'CR': r'^[0-9]{4,5}$',
    'CU': r'^[0-9]{5}$',
    'CV': r'^[0-9]{4}$',
    'CX': r'^[0-9]{4}$',
    'CY': r'^[0-9]{4}$',
    'CZ': r'^[0-9]{5}$',
    'DE': r'^[0-9]{5}$',
    'DK': r'^[0-9]{4}$',
    'DO': r'^[0-9]{5}$',
    'DZ': r'^[0-9]{5}$',
    'EC': r'^EC[0-9]{6}$',
    'EE': r'^[0-9]{5}$',
    'EG': r'^[0-9]{5}$',
    'ES': r'^[0-9]{5}$',
    'ET': r'^[0-9]{4}$',
    'FI': r'^[0-9]{5}$',
    'FK': r'^[A-Z]{4}[0-9][A-Z]{2}$',
    'FM': r'^[0-9]{5}(-[0-9]{4})?$',
    'FO': r'^[0-9]{3}$',
    'FR': r'^[0-9]{5}$',
    'GA': r'^[0-9]{2}.*[0-9]{2}$',
    'GB': r'^[A-Z][A-Z0-9]{1,3}[0-9][A-Z]{2}$',
    'GE': r'^[0-9]{4}$',
    'GF': r'^[0-9]{5}$',
    'GG': r'^([A-Z]{2}[0-9]{2,3}[A-Z]{2})$',
    'GI': r'^GX111AA$',
    'GL': r'^[0-9]{4}$',
    'GP': r'^[0-9]{5}$',
    'GR': r'^[0-9]{5}$',
    'GS': r'^SIQQ1ZZ$',
    'GT': r'^[0-9]{5}$',
    'GU': r'^[0-9]{5}$',
    'GW': r'^[0-9]{4}$',
    'HM': r'^[0-9]{4}$',
    'HN': r'^[0-9]{5}$',
    'HR': r'^[0-9]{5}$',
    'HT': r'^[0-9]{4}$',
    'HU': r'^[0-9]{4}$',
    'ID': r'^[0-9]{5}$',
    'IL': r'^[0-9]{7}$',
    'IM': r'^IM[0-9]{2,3}[A-Z]{2}$$',
    'IN': r'^[0-9]{6}$',
    'IO': r'^[A-Z]{4}[0-9][A-Z]{2}$',
    'IQ': r'^[0-9]{5}$',
    'IR': r'^[0-9]{5}-[0-9]{5}$',
    'IS': r'^[0-9]{3}$',
    'IT': r'^[0-9]{5}$',
    'JE': r'^JE[0-9]{2}[A-Z]{2}$',
    'JM': r'^JM[A-Z]{3}[0-9]{2}$',
    'JO': r'^[0-9]{5}$',
    'JP': r'^[0-9]{3}-?[0-9]{4}$',
    'KE': r'^[0-9]{5}$',
    'KG': r'^[0-9]{6}$',
    'KH': r'^[0-9]{5}$',
    'KR': r'^[0-9]{3}-?[0-9]{3}$',
    'KY': r'^KY[0-9]-[0-9]{4}$',
    'KZ': r'^[0-9]{6}$',
    'LA': r'^[0-9]{5}$',
    'LB': r'^[0-9]{8}$',
    'LI': r'^[0-9]{4}$',
    'LK': r'^[0-9]{5}$',
    'LR': r'^[0-9]{4}$',
    'LS': r'^[0-9]{3}$',
    'LT': r'^(LT-)?[0-9]{5}$',
    'LU': r'^[0-9]{4}$',
    'LV': r'^LV-[0-9]{4}$',
    'LY': r'^[0-9]{5}$',
    'MA': r'^[0-9]{5}$',
    'MC': r'^980[0-9]{2}$',
    'MD': r'^MD-?[0-9]{4}$',
    'ME': r'^[0-9]{5}$',
    'MF': r'^[0-9]{5}$',
    'MG': r'^[0-9]{3}$',
    'MH': r'^[0-9]{5}$',
    'MK': r'^[0-9]{4}$',
    'MM': r'^[0-9]{5}$',
    'MN': r'^[0-9]{5}$',
    'MP': r'^[0-9]{5}$',
    'MQ': r'^[0-9]{5}$',
    'MT': r'^[A-Z]{3}[0-9]{4}$',
    'MV': r'^[0-9]{4,5}$',
    'MX': r'^[0-9]{5}$',
    'MY': r'^[0-9]{5}$',
    'MZ': r'^[0-9]{4}$',
    'NA': r'^[0-9]{5}$',
    'NC': r'^[0-9]{5}$',
    'NE': r'^[0-9]{4}$',
    'NF': r'^[0-9]{4}$',
    'NG': r'^[0-9]{6}$',
    'NI': r'^[0-9]{3}-[0-9]{3}-[0-9]$',
    'NL': r'^[0-9]{4}[A-Z]{2}$',
    'NO': r'^[0-9]{4}$',
    'NP': r'^[0-9]{5}$',
    'NZ': r'^[0-9]{4}$',
    'OM': r'^[0-9]{3}$',
    'PA': r'^[0-9]{6}$',
    'PE': r'^[0-9]{5}$',
    'PF': r'^[0-9]{5}$',
    'PG': r'^[0-9]{3}$',
    'PH': r'^[0-9]{4}$',
    'PK': r'^[0-9]{5}$',
    'PL': r'^[0-9]{2}-?[0-9]{3}$',
    'PM': r'^[0-9]{5}$',
    'PN': r'^[A-Z]{4}[0-9][A-Z]{2}$',
    'PR': r'^[0-9]{5}$',
    'PT': r'^[0-9]{4}(-?[0-9]{3})?$',
    'PW': r'^[0-9]{5}$',
    'PY': r'^[0-9]{4}$',
    'RE': r'^[0-9]{5}$',
    'RO': r'^[0-9]{6}$',
    'RS': r'^[0-9]{5}$',
    'RU': r'^[0-9]{6}$',
    'SA': r'^[0-9]{5}$',
    'SD': r'^[0-9]{5}$',
    'SE': r'^[0-9]{5}$',
    'SG': r'^([0-9]{2}|[0-9]{4}|[0-9]{6})$',
    'SH': r'^(STHL1ZZ|TDCU1ZZ)$',
    'SI': r'^(SI-)?[0-9]{4}$',
    'SK': r'^[0-9]{5}$',
    'SM': r'^[0-9]{5}$',
    'SN': r'^[0-9]{5}$',
    'SV': r'^01101$',
    'SZ': r'^[A-Z][0-9]{3}$',
    'TC': r'^TKCA1ZZ$',
    'TD': r'^[0-9]{5}$',
    'TH': r'^[0-9]{5}$',
    'TJ': r'^[0-9]{6}$',
    'TM': r'^[0-9]{6}$',
    'TN': r'^[0-9]{4}$',
    'TR': r'^[0-9]{5}$',
    'TT': r'^[0-9]{6}$',
    'TW': r'^[0-9]{5}$',
    'UA': r'^[0-9]{5}$',
    'US': r'^[0-9]{5}(-[0-9]{4}|-[0-9]{6})?$',
    'UY': r'^[0-9]{5}$',
    'UZ': r'^[0-9]{6}$',
    'VA': r'^00120$',
    'VC': r'^VC[0-9]{4}',
    'VE': r'^[0-9]{4}[A-Z]?$',
    'VG': r'^VG[0-9]{4}$',
    'VI': r'^[0-9]{5}$',
    'VN': r'^[0-9]{6}$',
    'WF': r'^[0-9]{5}$',
    'XK': r'^[0-9]{5}$',
    'YT': r'^[0-9]{5}$',
    'ZA': r'^[0-9]{4}$',
    'ZM': r'^[0-9]{5}$',
}