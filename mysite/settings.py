from pathlib import Path
#import environ
import os

# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = False#env('DEBUG')
SECRET_KEY = '!4ois0xd2#h+0@8$zrp2u92s@w#27q$3ue1&2x$yy9@ms44gso'

ALLOWED_HOSTS = ['.vercel.app']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'it_works'
]

ROOT_URLCONF = 'mysite.urls'

# Alternatively could set to look for vercel
# and run wgsi application full string name then

WSGI_APPLICATION = 'mysite.wsgi.application'

# Reset databases, you could configure this separately
# to use a cloud db provider like firebase, supabase,
# rackspace etc to work with your app in vercel
DATABASES = {} 

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
# Configures the staticfiles directory to serve
# static files from /static/ on our deployment
STATIC_ROOT = os.path.join(
    BASE_DIR, 'staticfiles', 'static')

STATIC_URL = '/static/'
