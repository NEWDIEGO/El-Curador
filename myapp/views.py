from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login

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

def register(request):
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
        return redirect(reverse('paciente_dashboard'))
    
    return render(request, 'register.html')

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