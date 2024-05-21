from django.contrib import admin
from .models import Cliente,Usuario,Especialidad,Pago,HistorialAtencion,HorariosAtencion,Tecnico,Reserva
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Especialidad)
admin.site.register(Pago)
admin.site.register(HistorialAtencion)
admin.site.register(HorariosAtencion)
admin.site.register(Tecnico)
admin.site.register(Reserva)