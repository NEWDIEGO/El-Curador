from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.user.username

class Especialista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=10, null=True, blank=True)
    prevision = models.CharField(max_length=20, null=True, blank=True)
    comentario = models.TextField(null=True, blank=True)  # Agregar el campo de comentario

    def __str__(self):
        return self.usuario.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if not instance.is_superuser:
        instance.perfil.save()

class Reserva(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    especialista = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.CharField(max_length=5)
    valor_consulta = models.DecimalField(max_digits=10, decimal_places=2)
    numero_reserva = models.AutoField(primary_key=True)