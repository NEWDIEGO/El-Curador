# Generated by Django 5.0.4 on 2024-05-29 01:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_perfil_comentario_perfil_genero_perfil_prevision_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('especialista', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('hora', models.CharField(max_length=5)),
                ('valor_consulta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('numero_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]