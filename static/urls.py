from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.login_view, name='home'),  # Página principal que redirige al login
    path('login/', views.login_view, name='login'),  # Vista de login
    path('logout/', views.logout_view, name='logout'),  # Vista de logout
    path('custom_login/', views.custom_login, name='custom_login'),  # Vista de login personalizada
    path('registrar/', views.registrar, name='registrar'),  # Vista de registro
    path('ver-inscritos/', views.ver_inscritos, name='ver_inscritos'),  # Vista para ver inscritos
    
    # URLs para restablecer contraseña
    path('NewPass2/', auth_views.PasswordResetView.as_view(template_name='NewPass.html'), name='password_reset'),
    path('NewPass2_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('NewPass2_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    
    # Incluye las URLs de autenticación predeterminadas de Django
    path('', include('django.contrib.auth.urls')),
    
    # Vistas del dashboard y otras funcionalidades
    path('paciente_dashboard/', views.paciente_dashboard, name='paciente_dashboard'),
    path('especialista_dashboard/', views.especialista_dashboard, name='especialista_dashboard'),
    path('paciente_reserva/', views.paciente_reserva, name='paciente_reserva'),
    path('paciente_perfil/', views.PacientePerfil, name='paciente_perfil'),
    path('especialista/', views.especialista, name='especialista'),
    path('especialista_perfil/', views.especialista_perfil, name='especialista_perfil'),
    path('especialista_lista/', views.especialista_lista, name='especialista_lista'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
