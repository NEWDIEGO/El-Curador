"""
URL configuration for mysite project.

La lista urlpatterns en ruta URLs a vistas. Para más información, por favor consulta:
https://docs.djangoproject.com/en/5.0/topics/http/urls/
Ejemplos:
Vistas de función
1. Añadir una importación: from my_app import views
2. Añadir una URL a urlpatterns: path('', views.home, name='home')
Vistas basadas en clases
1. Añadir una importación: from other_app.views import Home
2. Añadir una URL a urlpatterns: path('', Home.as_view(), name='home')
Incluyendo otra configuración de URL
1. Importar la función include(): from django.urls import include, path
2. Añadir una URL a urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
