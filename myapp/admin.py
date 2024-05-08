from django.contrib import admin
from .models import MiModelo
from .models import Project, Task
# Register your models here.
class MiModeloAdmin(admin.ModelAdmin):
    list_display = ('campo1', 'campo2', 'campo3')  # Campos que quieres mostrar en la lista
    search_fields = ['campo1', 'campo2']  # Campos por los que se puede buscar
    list_filter = ('campo2',)  # Campos para filtrar en la barra lateral

admin.site.register(MiModelo, MiModeloAdmin)
admin.site.register(Project)
