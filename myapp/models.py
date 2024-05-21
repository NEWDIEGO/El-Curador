from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    run = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=50, blank=True, null=True)
    apellido_materno = models.CharField(max_length=50, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    vigencia = models.CharField(max_length=7, blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Especialidad(models.Model):
    id_especialidad = models.IntegerField(primary_key=True)
    especialidad = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especialidad'


class HistorialAtencion(models.Model):
    id_historial_atencion = models.IntegerField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_tecnico = models.ForeignKey('Tecnico', models.DO_NOTHING, db_column='id_tecnico', blank=True, null=True)
    id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_reserva', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_atencion'


class HorariosAtencion(models.Model):
    id_horario_atencion = models.IntegerField(primary_key=True)
    dia_semana = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    duracion_cita = models.IntegerField(blank=True, null=True)
    id_tecnico = models.ForeignKey('Tecnico', models.DO_NOTHING, db_column='id_tecnico', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horarios_atencion'


class Pago(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    numero_reserva = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_tecnico = models.ForeignKey('Tecnico', models.DO_NOTHING, db_column='id_tecnico', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pago'


class Reserva(models.Model):
    id_reserva = models.IntegerField(primary_key=True)
    nro_reserva = models.IntegerField(blank=True, null=True)
    agendar_hora = models.DateTimeField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_horario_atencion = models.ForeignKey(HorariosAtencion, models.DO_NOTHING, db_column='id_horario_atencion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reserva'


class Tecnico(models.Model):
    id_tecnico = models.IntegerField(primary_key=True)
    run = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=50, blank=True, null=True)
    apellido_materno = models.CharField(max_length=50, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    id_especialidad = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='id_especialidad', blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnico'


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    contrasena = models.CharField(max_length=50, blank=True, null=True)
    vigencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'