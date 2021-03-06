# -*- coding: utf-8 -*-
"""
Django settings for MyDjango project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+&_1novz_lfho8ujb1tq!p2)dk&w=7xmt&^fxome2(ohlk%kv!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

# 允许的主机名
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'wechat',
    # 'rest_framework',
    # 'rest_framework_swagger',
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

ROOT_URLCONF = 'MyDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'MyDjango.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


# 设置的static file的起始url，这个只是在template里边引用到，这个参数和MEDIA_URL的含义相同。
STATIC_URL = '/static/'  # html中引用时 用到此url

# 当运行 python manage.py collectstatic 的时候
# STATIC_ROOT 文件夹 是用来将所有STATICFILES_DIRS中所有文件夹中的文件，以及各app中static中的文件都复制过来
# 把这些文件放到一起是为了用apache等部署的时候更方便
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")  # uwign时使用的是STATIC_ROOT; 自带服务器使用的是STATICFILES_DIRS

# 其它 存放静态文件的文件夹，可以用来存放项目中公用的静态文件，里面不能包含 STATIC_ROOT
# 如果不想用 STATICFILES_DIRS 可以不用，都放在 app 里的 static 中也可以

#   运行前要先收集静态文件 python manage.py collectstatic
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),  # 声明静态文件 文件夹位置
                    # os.path.join(BASE_DIR, "media1"),
                    # os.path.join(BASE_DIR,"myapp", "static1"),
                    # os.path.join(BASE_DIR, "static_files"),
                    ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)

# #不习惯REST_FRAMEWORK 还是使用传统api接口吧
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    # 'DEFAULT_RENDERER_CLASSES' :('rest_framework.renderers.JSONRenderer',)
    # 'PAGE_SIZE': 10
}

# #不习惯swagger 还是使用apidoc吧
# # swagger 配置项
# SWAGGER_SETTINGS = {
#     # 基础样式
#     'SECURITY_DEFINITIONS': {
#         "basic":{
#             'type': 'basic'
#         }
#     },
#     # 如果需要登录才能够查看接口文档, 登录的链接使用restframework自带的.
#     'LOGIN_URL': 'rest_framework:login',
#     'LOGOUT_URL': 'rest_framework:logout',
#     # 'DOC_EXPANSION': None,
#     # 'SHOW_REQUEST_HEADERS':True,
#     # 'USE_SESSION_AUTH': True,
#     # 'DOC_EXPANSION': 'list',
#     # 接口文档中方法列表以首字母升序排列
#     'APIS_SORTER': 'alpha',
#     # 如果支持json提交, 则接口文档中包含json输入框
#     'JSON_EDITOR': True,
#     # 方法列表字母排序
#     'OPERATIONS_SORTER': 'alpha',
#     'VALIDATOR_URL': None,
# }
