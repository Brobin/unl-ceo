import os

LOCAL_SECRET_KEY = '(pub^&ska%=&902j#pe$2la=$8r_8p*z-x*+s^k5x7-@h&fkw9'

LOCAL_ALLOWED_HOSTS = ['*']

LOCAL_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.sqlite3'),
    }
}

LOCAL_DEBUG = True

LOCAL_TEMPLATE_DEBUG = True

LOCAL_STATIC_ROOT = './static'

LOCAL_STATIC_URL = '/static/'

LOCAL_MEDIA_ROOT = './ceo/static/media'

LOCAL_MEDIA_URL = '/media/'