from django.contrib import admin
from .models import Cliente, Especialista, Especialidad, Pago, HorariosAtencion, Reserva, HistorialAtencion

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre', 'apellido_paterno', 'correo')

@admin.register(Especialista)
class EspecialistaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre', 'apellido_paterno', 'especialidad')

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('numero_reserva', 'fecha', 'costo', 'especialista')

@admin.register(HorariosAtencion)
class HorariosAtencionAdmin(admin.ModelAdmin):
    list_display = ('dia_semana', 'fecha', 'hora_inicio', 'hora_fin', 'especialista')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nro_reserva', 'agendar_hora', 'estado', 'cliente', 'horario_atencion')

@admin.register(HistorialAtencion)
class HistorialAtencionAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'especialista', 'reserva', 'fecha')
