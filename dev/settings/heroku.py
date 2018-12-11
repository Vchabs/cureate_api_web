import django_heroku

from .base import *

DEBUG = bool(os.environ.get('DEBUG',False))

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
HTTPS='on'
ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'

# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.RedisCache',
#         'LOCATION': [os.environ['REDIS_SERVER'] + ':6379'],
#         'OPTIONS': {
#             'DB': 0,
#             'PARSER_CLASS': 'redis.connection.HiredisParser',
#             'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
#             'CONNECTION_POOL_CLASS_KWARGS': {
#                 'max_connections': 200,
#                 'timeout': 20,
#             },
#             'MAX_CONNECTIONS': 1000,
#             'PICKLE_VERSION': -1,
#         },
#     },
# }

# DATABASES = {
#         'default': {
#             'ENGINE': os.environ['DATABASE_ENGINE'],
#             'NAME': os.environ['DATABASE_NAME'], 
#             'USER': os.environ['DATABASE_USER'],
#             'PASSWORD': os.environ['DATABASE_PASSWORD'], 
#             'HOST':os.environ['DATABASE_HOST'],    
#             'PORT': os.environ['DATABASE_PORT'] 
#         }
#     }
# CONN_MAX_AGE=30

django_heroku.settings(locals())
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)



STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

ACME_CHALLENGE_CONTENT = os.environ.get('ACME_CHALLENGE_CONTENT',"FAIL")
