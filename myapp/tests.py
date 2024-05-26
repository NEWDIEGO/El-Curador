from django.test import TestCase
from django.contrib.auth.models import User
from .models import Perfil

class PerfilTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        Perfil.objects.create(usuario=user, fecha_nacimiento='1990-01-01', genero='Masculino', prevision='FONASA')

    def test_perfil_creation(self):
        perfil = Perfil.objects.get(usuario__username='testuser')
        self.assertEqual(perfil.genero, 'Masculino')
