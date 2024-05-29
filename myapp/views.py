
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Perfil
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Reserva
from django.views.decorators.http import require_POST

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            return render(request, 'login.html', {'error': 'Campos vacíos y/o incompletos'})

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
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
        nombre = request.POST.get('nombre')
        apellido_paterno = request.POST.get('apellidoPaterno')
        apellido_materno = request.POST.get('apellidoMaterno')
        email = request.POST.get('correo')
        password = request.POST.get('contraseña')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        genero = request.POST.get('genero')
        prevision = request.POST.get('prevision')

        # Combinar los nombres y apellidos para crear el username
        username = f"{nombre}{apellido_paterno}{apellido_materno}".lower().replace(" ", "")

        # Depuración para verificar los datos que se están recibiendo
        print(f"Nombre: {nombre}, Apellido Paterno: {apellido_paterno}, Apellido Materno: {apellido_materno}, Email: {email}, Username: {username}")

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = nombre
            user.last_name = f"{apellido_paterno} {apellido_materno}"
            user.save()

            # Depuración adicional
            user_refresh = User.objects.get(username=username)
            print(f"Refreshed User: {user_refresh.username}, First Name: {user_refresh.first_name}, Last Name: {user_refresh.last_name}, Email: {user_refresh.email}")

            # Verificar que los datos se guardaron correctamente
            print(f"User saved: {user.username}, First Name: {user.first_name}, Last Name: {user.last_name}, Email: {user.email}")

            # Crear perfil asociado
            perfil = Perfil.objects.create(
                usuario=user,
                fecha_nacimiento=fecha_nacimiento,
                genero=genero,
                prevision=prevision
            )
            perfil.save()

            messages.success(request, 'Paciente registrado exitosamente.')
            return redirect(reverse('login'))
        except Exception as e:
            messages.error(request, f"Error al registrar usuario: {e}")
            print(f"Error: {e}")

    return render(request, 'registrar.html')


@login_required
def paciente_dashboard(request):
    user = request.user
    print(f"User: {user.username}, First Name: {user.first_name}, Last Name: {user.last_name}, Email: {user.email}")
    nombre_usuario = f"{user.first_name } {user.last_name }".strip() if user.first_name and user.last_name else user.username
    return render(request, 'PacienteLogin.html', {'nombre_usuario': nombre_usuario})

@login_required
def especialista_dashboard(request):
    return render(request, 'EspecialistaLogin.html')

@login_required
def paciente_reserva(request):
    if request.method == 'POST':
        especialista = request.POST['especialista']
        fecha = request.POST['fecha']
        hora = request.POST['hora']
        valor_consulta = 50000  # Valor fijo para la consulta
        especialidades = {
            'medicina_general': 'Medicina General (Dr. Chopper)',
            'nutricionista': 'Nutricionista (Dra. Kureha)',
            'dentista': 'Dentista (Dr. Hiruluk)'
        }

        reserva = Reserva.objects.create(
            paciente=request.user,
            especialista=especialidades[especialista],
            especialidad=especialista.replace('_', ' ').title(),
            fecha=fecha,
            hora=hora,
            valor_consulta=valor_consulta
        )

        return redirect('confirmacion_reserva', reserva_id=reserva.numero_reserva)

    return render(request, 'PacienteReserva.html')

@login_required
def paciente_perfil(request):
    user = request.user

    # Verificar si el perfil existe, y si no, crearlo
    perfil, created = Perfil.objects.get_or_create(usuario=user)
    
    nombre_completo = f"{user.first_name} {user.last_name}"
    fecha_nacimiento = perfil.fecha_nacimiento.strftime("%d/%m/%Y") if perfil.fecha_nacimiento else "No especificada"

    contexto = {
        'nombre_completo': nombre_completo,
        'fecha_nacimiento': fecha_nacimiento,
        'correo': user.email,
        'comentario': perfil.comentario
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
    
@login_required
def generar_pdf(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    template_path = 'ReservaPDF.html'
    context = {'reserva': reserva}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reserva_{reserva.numero_reserva}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Hubo un error al generar el PDF <pre>' + html + '</pre>')
    return response

@login_required
def confirmacion_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    return render(request, 'ConfirmacionReserva.html', {'reserva': reserva})

@login_required
def paciente_lista_reservas(request):
    reservas = Reserva.objects.filter(paciente=request.user)
    return render(request, 'PacienteLista.html', {'reservas': reservas})

@login_required
def paciente_anula_reserva(request):
    reservas = Reserva.objects.filter(paciente=request.user)
    return render(request, 'PacienteAnula.html', {'reservas': reservas})

@require_POST
@login_required
def anular_reserva(request):
    reserva_id = request.POST.get('reserva_id')
    try:
        reserva = Reserva.objects.get(numero_reserva=reserva_id, paciente=request.user)
        reserva.delete()
        messages.success(request, 'Hora anulada con éxito')
    except Reserva.DoesNotExist:
        messages.error(request, 'No se pudo anular la reserva')
    return redirect('paciente_anula_reserva')