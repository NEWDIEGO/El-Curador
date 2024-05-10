from django.urls import path, include
from . import views
"""
urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.hello, name='home'),  # Esto manejará la ruta raíz
]
"""
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', include('django.contrib.auth.urls')),  # Incluye las URLs de autenticación
    path('', views.login_view, name='home'),
    path('register/', views.register, name='register'),
]