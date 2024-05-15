from django.contrib import admin
from .models import Paciente, Especialista

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha_nacimiento')

class EspecialistaAdmin(admin.ModelAdmin):
    list_display = ('user', 'especialidad')

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Especialista, EspecialistaAdmin)

# Personalización del sitio de administración
admin.site.site_header = "Administración de la Clínica"
admin.site.site_title = "Administración de la Clínica"
admin.site.index_title = "Panel de Administración"

# Reorganizar el orden de los modelos
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'Administración de la Clínica'
    site_title = 'Administración de la Clínica'
    index_title = 'Panel de Administración'

    def get_app_list(self, request):
        app_list = super(MyAdminSite, self).get_app_list(request)
        for app in app_list:
            if app['name'] == 'YourAppName':
                app['models'].sort(key=lambda x: x['name'])
        return app_list

admin_site = MyAdminSite()
admin_site.register(Paciente, PacienteAdmin)
admin_site.register(Especialista, EspecialistaAdmin)