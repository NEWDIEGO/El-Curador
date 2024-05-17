from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Especialista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha_nacimiento')  # Asegúrate de que 'fecha_nacimiento' está definido en el modelo

class EspecialistaAdmin(admin.ModelAdmin):
    list_display = ('user', 'especialidad')  # Asegúrate de que 'especialidad' está definido en el modelo

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
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Especialista, EspecialistaAdmin)

class PacienteAdmin(admin.ModelAdmin):
    pass


class EspecialistaAdmin(admin.ModelAdmin):
    pass