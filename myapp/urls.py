from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('login/', views.custom_login, name='login'),
    path('', include('django.contrib.auth.urls')),  # Incluye las URLs de autenticación
    path('', views.login_view, name='home'),
    path('register/', views.register, name='register'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='NewPass.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('PacienteLogin/', views.paciente_dashboard, name='PacienteLogin'),
    path('paciente_dashboard/', views.paciente_dashboard, name='paciente_dashboard'),
    path('especialista_dashboard/', views.especialista_dashboard, name='especialista_dashboard'),
]