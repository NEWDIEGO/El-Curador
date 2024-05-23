from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Perfil  # Asegúrate de que esta línea esté presente

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email or not password:
            return render(request, 'login.html', {'error': 'Campos vacíos y/o incompletos'})
        
        try:
            user = User.objects.get(username=email)
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('paciente_dashboard')  # Redirige a la página de perfil del paciente
            else:
                return render(request, 'login.html', {'error': 'Correo electrónico o contraseña incorrecta'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Usuario no inscrito'})
    else:
        return render(request, 'login.html')

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

@login_required
def paciente_dashboard(request):
    nombre_usuario = request.user.first_name
    return render(request, 'PacienteLogin.html', {'nombre_usuario': nombre_usuario})

@login_required
def especialista_dashboard(request):
    return render(request, 'EspecialistaLogin.html')

@login_required
def paciente_reserva(request):
    return render(request, 'PacienteReserva.html')

@login_required
def paciente_perfil(request):
    usuario = request.user
    perfil = usuario.perfil  # Asegúrate de que tienes un perfil relacionado con el usuario
    context = {
        'nombre_completo': f"{usuario.first_name} {usuario.last_name}",
        'fecha_nacimiento': perfil.fecha_nacimiento.strftime("%d/%m/%Y"),
        'correo': usuario.email,
        'genero': perfil.genero,
        'prevision': perfil.prevision,
        'comentario': perfil.comentario,
    }
    return render(request, 'PacientePerfil.html', context)

@csrf_exempt
@login_required
def guardar_comentario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comentario = data.get('comentario')
        perfil = request.user.perfil
        perfil.comentario = comentario
        perfil.save()
        return JsonResponse({'message': 'Comentario guardado con éxito'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def especialista(request):
    return render(request, 'especialista.html')

def especialista_perfil(request):
    return render(request, 'especialistaperfil.html')

def especialista_lista(request):
    return render(request, 'especialistalista.html')

def ver_inscritos(request):
    usuarios = User.objects.all()
    return render(request, 'ver_inscritos.html', {'usuarios': usuarios})

def logout_view(request):
    logout(request)
    return redirect('login')

# Definición de custom_login
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['correo']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('paciente_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    else:
        return render(request, 'login.html')
