import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ... Otras configuraciones ...

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ... Otras configuraciones ...

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'myapp' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ... Otras configuraciones ...
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Asegúrate de que esta línea esté presente
]
