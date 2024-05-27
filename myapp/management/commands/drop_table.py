from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Drops the specified tables from the database'

    def handle(self, *args, **kwargs):
        tables = [
            'myapp_especialista',
            'myapp_paciente',
            'myapp_perfil',
            'django_session',
            'sessions_session'  # Incluye cualquier otra tabla problemática aquí
        ]
        with connection.cursor() as cursor:
            for table in tables:
                cursor.execute(f"DROP TABLE IF EXISTS {table};")
        self.stdout.write(self.style.SUCCESS('Successfully dropped specified tables'))
