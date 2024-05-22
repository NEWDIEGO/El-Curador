INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Asegúrate de que esto es exactamente igual al nombre de la carpeta de tu app
    'Aplicaciones.Usuario'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_mysql',
        'USER': 'root',
        'PASSWORD': 'Holamundo-123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}