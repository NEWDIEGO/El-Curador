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
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

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
                try:
                    # Intenta acceder al perfil del usuario
                    user.perfil
                    return redirect('paciente_dashboard')
                except Perfil.DoesNotExist:
                    messages.error(request, 'Usuario no tiene un perfil asociado.')
                    return redirect('login')
            else:
                return render(request, 'login.html', {'error': 'Correo electrónico o contraseña incorrecta'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Usuario no inscrito'})
    else:
        return render(request, 'login.html')

def registrar(request):
    if request.method == 'POST':
        username = request.POST.get('correo')
        password = request.POST.get('contraseña')
        first_name = request.POST.get('nombre')
        last_name = request.POST.get('apellidoPaterno') + ' ' + request.POST.get('apellidoMaterno')
        email = request.POST.get('correo')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        genero = request.POST.get('genero')
        prevision = request.POST.get('prevision')

        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # Crear perfil asociado
            Perfil.objects.create(
                usuario=user,
                fecha_nacimiento=fecha_nacimiento,
                genero=genero,
                prevision=prevision
            )

            messages.success(request, 'Paciente registrado exitosamente.')
            return redirect(reverse('login'))  # Redirige a la vista de login
        except Exception as e:
            messages.error(request, 'Error al registrar usuario: {}'.format(e))

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
    user = request.user
    perfil = get_object_or_404(Perfil, usuario=user)

    fecha_nacimiento = perfil.fecha_nacimiento.strftime("%d/%m/%Y") if perfil.fecha_nacimiento else "No especificada"

    contexto = {
        'nombre_completo': f"{user.first_name} {user.last_name}",
        'fecha_nacimiento': fecha_nacimiento,
        'correo': user.email
    }

    return render(request, 'PacientePerfil.html', contexto)

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
