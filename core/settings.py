"""
Django settings for simpleui_demo project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '&%up9@!s_$$4(qurnori=vit2#kg!bzs$_+m64^j$2-vzibx&p'

DEBUG = True

ALLOWED_HOSTS = ['*', ]

INSTALLED_APPS = [
    'core',
]

ROOT_URLCONF = 'core.urls'

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True



