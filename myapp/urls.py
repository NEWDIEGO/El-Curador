from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.hello, name='home'),  # Esto manejará la ruta raíz
]