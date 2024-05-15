from django.urls import path
from . import views
from myapp.views import vista_medico
from myapp.views import Vista_EspecialistaPerfil
from myapp.views import Vista_EspecialistaLista
urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
    path('Especialista/', vista_medico),
    path('Especialista/Perfil/', Vista_EspecialistaPerfil),
    path('Especialista/Lista_de_espera/', Vista_EspecialistaLista),
]