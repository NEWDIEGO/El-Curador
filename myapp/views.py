from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.db import IntegrityError
from django.apps import AppConfig

def login_view(request):
    # Asegúrate de que 'login.html' se encuentra en la carpeta 'templates' dentro de alguna app o en una ubicación que Django reconozca.
    return render(request, 'login.html')

def hello(request):
    # Retorna un mensaje simple usando HttpResponse.
    return HttpResponse("Bienvenidos a la clínica EL CURADOR")

def about(request):
    # Para un texto simple, sigue usando HttpResponse.
    return HttpResponse('About')

def user_login(request):
    # Asegúrate de que 'myapp/login.html' se encuentra en la carpeta 'templates/myapp' dentro de tu proyecto.
    return render(request, 'myapp/login.html')



def registrar(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        nombre = request.POST['nombre']
        apellidoPaterno = request.POST['apellidoPaterno']
        apellidoMaterno = request.POST['apellidoMaterno']
        correo = request.POST['correo']
        contraseña = request.POST['contraseña']
        fechaNacimiento = request.POST['fechaNacimiento']
        genero = request.POST['genero']
        
        # Crear el usuario
        user = User.objects.create_user(
            username=correo,
            email=correo,
            password=contraseña,
            first_name=nombre,
            last_name=apellidoPaterno
        )
        
        # Guardar información adicional
        user.profile.apellidoMaterno = apellidoMaterno
        user.profile.fechaNacimiento = fechaNacimiento
        user.profile.genero = genero
        user.profile.rut = rut
        user.save()
        
        # Iniciar sesión y redirigir
        login(request, user)
        return redirect('login')  # Esto redirige al login después de registrarse
    return render(request, 'registrar.html')

def process_registration(request):
    if request.method == 'POST':
        local_part = request.POST['correo']
        domain = request.POST['dominio']
        full_email = local_part + domain

def paciente_login(request):
    return render(request, 'PacienteLogin.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Redireccionando a:", reverse('paciente_dashboard'))
            return redirect(reverse('paciente_dashboard'))
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    else:
        return render(request, 'login.html')

def paciente_dashboard(request):
    return render(request, 'PacienteLogin.html')

@login_required
def paciente_dashboard(request):
    return render(request, 'PacienteLogin.html')

@login_required
def especialista_dashboard(request):
    return render(request, 'EspecialistaLogin.html')

@login_required
def paciente_reserva(request):
    return render(request, 'PacienteReserva.html')

@login_required
def PacientePerfil(request):
    # Aquí puedes pasar los datos del perfil del usuario si es necesario
    return render(request, 'PacientePerfil.html')

def especialista(request):
    return render(request, 'especialista.html')

def especialista_perfil(request):
    return render(request, 'especialistaperfil.html')

def especialista_lista(request):
    return render(request, 'especialistalista.html')

def registrar(request):
    if request.method == 'POST':
        username = request.POST['correo']
        password = request.POST['contraseña']
        first_name = request.POST['nombre']
        last_name = request.POST['apellidoPaterno'] + ' ' + request.POST['apellidoMaterno']
        email = request.POST['correo']
        
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, 'Paciente registrado exitosamente.')  # Agrega un mensaje de éxito
            return redirect('login')  # Redirige al login
        except Exception as e:
            messages.error(request, 'Error al registrar usuario: {}'.format(e))  # Agrega un mensaje de error

    return render(request, 'registrar.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('PacienteLogin')  # Cambia esto por el nombre de la URL del dashboard de pacientes
        else:
            messages.error(request, "Correo y/o contraseña inválidas")
    return render(request, 'login.html')

def create_default_user():
    # Intenta obtener el usuario si existe, o crea uno nuevo si no existe
    user, created = User.objects.get_or_create(
        username='paciente',  # Asegúrate de que este es el nombre de usuario correcto que quieres verificar y crear
        defaults={
            'email': 'paciente@gmail.com',
            'password': 'Holamundo-123'  # Ten en cuenta que esto no establece la contraseña correctamente
        }
    )
    if created:
        user.set_password('Holamundo-123')  # Asegúrate de guardar la contraseña correctamente
        user.save()
        print("Usuario creado exitosamente.")
    else:
        print("El usuario ya existe.")

# Llama a esta función en algún lugar apropiado, como al inicio del servidor o dentro de una vista específica.
create_default_user()

def create_default_user():
    if not User.objects.filter(username='paciente').exists():
        User.objects.create_user('paciente', 'paciente@gmail.com', 'Holamundo-123')
    else:
        print("El usuario ya existe.")

def create_default_user():
    try:
        User.objects.create_user('paciente', 'paciente@gmail.com', 'Holamundo-123')
        print("Usuario creado exitosamente.")
    except IntegrityError as e:
        print(f"No se pudo crear el usuario debido a: {e}")

class TuAppConfig(AppConfig):
    name = 'tu_app'

    def ready(self):
        from . import signals  # importa tus señales si las usas
        self.create_default_user()

    @staticmethod
    def create_default_user():
        if not User.objects.filter(username='paciente').exists():
            User.objects.create_user('paciente', 'paciente@gmail.com', 'Holamundo-123')