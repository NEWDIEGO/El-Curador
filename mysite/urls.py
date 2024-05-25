from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp.admin import admin_site  # Importa tu sitio de administración personalizado

urlpatterns = [
    path('admin/', admin_site.urls),  # Usa el admin site personalizado
    path('', include('myapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)