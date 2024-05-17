from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import registrar
from .views import login_view
from myapp.views import user_login
from myapp.views import custom_login

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('login/', views.custom_login, name='login'),
    path('', include('django.contrib.auth.urls')),  # Incluye las URLs de autenticación
    path('', views.login_view, name='home'),
    path('registrar/', views.registrar, name='registrar'),
    path('NewPass2/', auth_views.PasswordResetView.as_view(template_name='NewPass.html'), name='password_reset'),
    path('NewPass2_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('NewPass2_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('paciente_login/', views.paciente_login, name='paciente_login'),
    path('paciente_dashboard/', views.paciente_dashboard, name='paciente_dashboard'),
    path('especialista_dashboard/', views.especialista_dashboard, name='especialista_dashboard'),
    path('paciente_dashboard/', views.paciente_dashboard, name='paciente_dashboard'),
    path('paciente_dashboard/', views.paciente_dashboard, name='PacienteLogin'),
    path('paciente_reserva/', views.paciente_reserva, name='PacienteReserva'),
    path('paciente_perfil/', views.PacientePerfil, name='PacientePerfil'),
    path('especialista/', views.especialista, name='especialista'),
    path('EspecialistaPerfil/', views.especialista_perfil, name='EspecialistaPerfil'),
    path('EspecialistaLista/', views.especialista_lista, name='EspecialistaLista'),
    path('login/', login_view, name='login'),
    path('login/', custom_login, name='login'),
]