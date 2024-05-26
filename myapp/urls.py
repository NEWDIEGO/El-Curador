# En mysite/urls.py
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registrar/', views.registrar, name='registrar'),
    path('ver-inscritos/', views.ver_inscritos, name='ver_inscritos'),

    # URLs para restablecer contraseña
    path('NewPass2/', auth_views.PasswordResetView.as_view(template_name='NewPass.html'), name='password_reset'),
    path('NewPass2_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('NewPass2_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    # URLs para administrador
    path('menu-admin/', views.menu_admin, name='menu_admin'),
    path('gestionar_usuarios/', views.gestionar_usuarios, name='gestionar_usuarios'),
    path('asignar_horarios/', views.asignar_horarios, name='asignar_horarios'),
    path('ver_informes/', views.ver_informes, name='ver_informes'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('modificar_usuario/<int:id>/', views.modificar_usuario, name='modificar_usuario'),
    path('eliminar_usuario/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),

    # URLs para especialista
    path('especialista/', views.especialista, name='especialista'),
    path('especialista_perfil/', views.especialista_perfil, name='especialista_perfil'),
    path('especialista_lista/', views.especialista_lista, name='especialista_lista'),

    # URLs para paciente
    path('paciente_dashboard/', views.paciente_dashboard, name='paciente_dashboard'),
    path('paciente_reserva/', views.paciente_reserva, name='paciente_reserva'),
    path('paciente_perfil/', views.paciente_perfil, name='paciente_perfil'),
    path('paciente_anula/', views.paciente_anula, name='paciente_anula'),

    path('guardar_comentario/', views.guardar_comentario, name='guardar_comentario'),
]
