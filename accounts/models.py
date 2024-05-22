from django.db import models

# Create your models here.
class Usuario(models.model):
    nombre =models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()