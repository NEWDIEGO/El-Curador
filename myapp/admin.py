from django.contrib import admin
from .models import Paciente, Especialista
from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha_nacimiento')

class Especialista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class EspecialistaAdmin(admin.ModelAdmin):
    list_display = ('user', 'especialidad')

admin.site.registrar(Paciente, PacienteAdmin)
admin.site.registrar(Especialista, EspecialistaAdmin)

# Personalización del sitio de administración
admin.site.site_header = "Administración de la Clínica"
admin.site.site_title = "Administración de la Clínica"
admin.site.index_title = "Panel de Administración"

# Reorganizar el orden de los modelos
class MyAdminSite(admin.AdminSite):
    site_header = _('Mi aplicación de administración')
    site_title = _('Mi sitio de admin')

    def get_app_list(self, request):
        """
        Retorna una lista modificada de aplicaciones, que agrupa a Paciente y Especialista bajo un nuevo título.
        """
        app_list = super().get_app_list(request)
        user_app = {'name': 'Usuario', 'app_label': 'usuario', 'models': []}

        for app in app_list:
            for model in app['models']:
                if model['object_name'] in ['Paciente', 'Especialista']:
                    user_app['models'].append(model)
                    app['models'].remove(model)
            if not app['models']:  # Si no quedan modelos, elimina la app
                app_list.remove(app)

        if user_app['models']:  # Si hay modelos bajo 'Usuario', añádelos
            app_list.insert(0, user_app)  # Puedes ajustar la posición según necesites

        return app_list

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Paciente, PacienteAdmin)
admin_site.register(Especialista, EspecialistaAdmin)
admin_site.register(User)  # Asegúrate de registrar cualquier otro modelo necesario

class PacienteAdmin(admin.ModelAdmin):
    pass


class EspecialistaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Especialista, EspecialistaAdmin)