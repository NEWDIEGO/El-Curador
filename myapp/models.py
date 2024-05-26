from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    run = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    prevision = models.CharField(max_length=20, choices=[('Fonasa', 'Fonasa'), ('Isapre', 'Isapre'), ('Colmena', 'Colmena')])

    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno

class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Especialista(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    run = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno

class Pago(models.Model):
    numero_reserva = models.IntegerField()
    fecha = models.DateField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    especialista = models.ForeignKey(Especialista, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pago {self.numero_reserva} - {self.especialista}"

class HorariosAtencion(models.Model):
    dia_semana = models.CharField(max_length=20)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    duracion_cita = models.IntegerField()
    especialista = models.ForeignKey(Especialista, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.dia_semana} - {self.especialista}"

class Reserva(models.Model):
    nro_reserva = models.IntegerField()
    agendar_hora = models.DateTimeField()
    estado = models.BooleanField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    horario_atencion = models.ForeignKey(HorariosAtencion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva {self.nro_reserva} - {self.cliente}"

class HistorialAtencion(models.Model):
    fecha = models.DateField()
    comentario = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    especialista = models.ForeignKey(Especialista, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

    def __str__(self):
        return f"Historial {self.cliente} - {self.especialista} - {self.fecha}"
