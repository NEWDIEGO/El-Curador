from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Paciente, Especialista, Perfil  # Importa los modelos necesarios

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha_nacimiento')

class EspecialistaAdmin(admin.ModelAdmin):
    list_display = ('user', 'especialidad')

# Personalización del sitio de administración
class MyAdminSite(admin.AdminSite):
    site_header = _('Administración de la Clínica')
    site_title = _('Panel de Administración de la Clínica')
    index_title = _('Panel de Administración')

    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        # Tu lógica personalizada aquí
        return app_list

admin_site = MyAdminSite(name='myadmin')

# Registro de modelos y administradores
admin_site.register(Paciente, PacienteAdmin)
admin_site.register(Especialista, EspecialistaAdmin)
admin_site.register(User)  # Registra User si es necesario

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha_nacimiento', 'genero', 'prevision')
"""
# Registrar en el admin site predeterminado
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Especialista, EspecialistaAdmin)
admin.site.register(Perfil, PerfilAdmin)
"""