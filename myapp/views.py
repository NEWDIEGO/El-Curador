from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import json
from .models import Cliente, Especialista, Especialidad, Pago, HorariosAtencion, Reserva, HistorialAtencion
from datetime import datetime

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
                return redirect('paciente_dashboard')
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

            Cliente.objects.create(
                usuario=user,
                fecha_nacimiento=fecha_nacimiento,
                genero=genero,
                prevision=prevision
            )

            messages.success(request, 'Paciente registrado exitosamente.')
            return redirect(reverse('login'))
        except Exception as e:
            messages.error(request, 'Error al registrar usuario: {}'.format(e))

    return render(request, 'registrar.html')

@login_required
def paciente_dashboard(request):
    nombre_usuario = request.user.first_name
    return render(request, 'paciente/PacienteLogin.html', {'nombre_usuario': nombre_usuario})

@login_required
def paciente_reserva(request):
    return render(request, 'paciente/PacienteReserva.html')

@login_required
def paciente_perfil(request):
    user = request.user
    cliente = Cliente.objects.get(usuario=user)
    fecha_nacimiento = cliente.fecha_nacimiento.strftime("%d/%m/%Y") if cliente.fecha_nacimiento else "No especificada"
    contexto = {
        'nombre_completo': f"{user.first_name} {user.last_name}",
        'fecha_nacimiento': fecha_nacimiento,
        'correo': user.email
    }
    return render(request, 'paciente/PacientePerfil.html', contexto)

@login_required
def paciente_anula(request):
    return render(request, 'paciente/PacienteAnula.html')

@login_required
def asignar_horarios(request):
    profesionales = Especialista.objects.all()
    
    if request.method == 'POST':
        profesional_id = request.POST.get('profesional')
        hora_inicio = request.POST.get('hora_inicio')
        hora_termino = request.POST.get('hora_termino')
        fecha_str = request.POST.get('fecha')
        duracion_cita = request.POST.get('duracion_cita')
        
        # Convertir fecha de string a datetime.date
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        dia_semana = fecha.strftime("%A")

        profesional = Especialista.objects.get(id=profesional_id)
        
        HorariosAtencion.objects.create(
            especialista=profesional,
            hora_inicio=hora_inicio,
            hora_fin=hora_termino,
            fecha=fecha,
            duracion_cita=duracion_cita,
            dia_semana=dia_semana
        )
        
        messages.success(request, 'Horario asignado correctamente.')
        return redirect('menu_admin')
    
    return render(request, 'administrador/asignar_horarios.html', {'profesionales': profesionales})

def ver_inscritos(request):
    usuarios = User.objects.all()
    return render(request, 'ver_inscritos.html', {'usuarios': usuarios})

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

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def menu_admin(request):
    return render(request, 'administrador/menu_admin.html')

@login_required
def gestionar_usuarios(request):
    usuarios = Especialista.objects.all()
    return render(request, 'administrador/gestionar_usuarios.html', {'usuarios': usuarios})


    profesionales = Especialista.objects.all()
    
    if request.method == 'POST':
        profesional_id = request.POST.get('profesional')
        hora_inicio = request.POST.get('hora_inicio')
        hora_termino = request.POST.get('hora_termino')
        fecha = request.POST.get('fecha')
        duracion_cita = request.POST.get('duracion_cita')
        dia_semana = fecha.strftime("%A")

        profesional = Especialista.objects.get(id=profesional_id)
        
        HorariosAtencion.objects.create(
            especialista=profesional,
            hora_inicio=hora_inicio,
            hora_fin=hora_termino,
            fecha=fecha,
            duracion_cita=duracion_cita,
            dia_semana=dia_semana
        )
        
        messages.success(request, 'Horario asignado correctamente.')
        return redirect('menu_admin')
    
    return render(request, 'administrador/asignar_horarios.html', {'profesionales': profesionales})


@login_required
def ver_informes(request):
    informes = HistorialAtencion.objects.select_related('cliente', 'especialista').all()
    return render(request, 'administrador/informes.html', {'informes': informes})

@login_required
def crear_usuario(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido_paterno = request.POST.get('apellido_paterno')
        apellido_materno = request.POST.get('apellido_materno')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        confirmar_contrasena = request.POST.get('confirmar_contrasena')
        telefono = request.POST.get('telefono')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        genero = request.POST.get('genero')
        especialidad_nombre = request.POST.get('especialidad')

        if contrasena != confirmar_contrasena:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('crear_usuario')

        try:
            user = User.objects.create_user(username=correo, email=correo, password=contrasena)
            user.first_name = nombre
            user.last_name = f"{apellido_paterno} {apellido_materno}"
            user.save()

            especialidad, created = Especialidad.objects.get_or_create(nombre=especialidad_nombre)

            Especialista.objects.create(
                usuario=user,
                run=rut,
                nombre=nombre,
                apellido_paterno=apellido_paterno,
                apellido_materno=apellido_materno,
                correo=correo,
                telefono=telefono,
                fecha_nacimiento=fecha_nacimiento,
                genero=genero,
                especialidad=especialidad
            )

            messages.success(request, 'Usuario especialista registrado exitosamente.')
            return redirect('menu_admin')
        except Exception as e:
            messages.error(request, f'Error al registrar usuario: {e}')
            return redirect('crear_usuario')
    else:
        especialidades = Especialidad.objects.all()
        return render(request, 'administrador/crear_usuario.html', {'especialidades': especialidades})


@login_required
def modificar_usuario(request, id=None):
    if id:
        try:
            usuario = Especialista.objects.get(id=id)
        except Especialista.DoesNotExist:
            messages.error(request, 'Usuario no encontrado.')
            return redirect('gestionar_usuarios')

        if request.method == 'POST':
            usuario.run = request.POST.get('run')
            usuario.nombre = request.POST.get('nombre')
            usuario.apellido_paterno = request.POST.get('apellido_paterno')
            usuario.apellido_materno = request.POST.get('apellido_materno')
            usuario.correo = request.POST.get('correo')
            usuario.telefono = request.POST.get('telefono')
            usuario.fecha_nacimiento = request.POST.get('fecha_nacimiento')
            usuario.genero = request.POST.get('genero')
            if request.POST.get('contrasena'):
                usuario.set_password(request.POST.get('contrasena'))
            usuario.save()
            messages.success(request, 'Usuario modificado exitosamente.')
            return redirect('gestionar_usuarios')
        else:
            return render(request, 'administrador/modificar_usuario.html', {'usuario': usuario})
    else:
        messages.error(request, 'ID de usuario no proporcionado.')
        return redirect('gestionar_usuarios')

@login_required
def eliminar_usuario(request, id):
    usuario = get_object_or_404(Especialista, id=id)
    usuario.delete()
    messages.success(request, 'Usuario eliminado exitosamente.')
    return redirect('gestionar_usuarios')

@login_required
def especialista(request):
    return render(request, 'especialista/especialista.html')

@login_required
def especialista_perfil(request):
    return render(request, 'especialista/EspecialistaPerfil.html')

@login_required
def especialista_lista(request):
    return render(request, 'especialista/EspecialistaLista.html')

@csrf_exempt
@login_required
def guardar_comentario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comentario = data.get('comentario')
        cliente = request.user.cliente
        cliente.comentario = comentario
        cliente.save()
        return JsonResponse({'message': 'Comentario guardado con éxito'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)
