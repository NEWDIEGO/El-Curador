from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.login, name='home'),  # Esto manejará la ruta raíz
]