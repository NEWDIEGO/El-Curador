from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('about/', views.about, name='about'),
    path('Especialista/', views.vista_medico, name='vista_medico'),
    path('Especialista/Perfil/', views.Vista_EspecialistaPerfil, name='vista_especialista_perfil'),
    path('Especialista/Lista_de_espera/', views.Vista_EspecialistaLista, name='vista_especialista_lista'),
    path('Especialista/Notificar/', views.Vista_EspecialistaNotificar, name='vista_especialista_notificar'),
    path('Lista_HorariosAtencion/', views.lista_HorariosAtencion, name='lista_HorariosAtencion'),
]