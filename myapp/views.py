from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        # Aquí manejas la lógica de verificación después de que el usuario envíe el formulario
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Aquí añadirías la lógica para verificar las credenciales del usuario
        if True:  # Supongamos que siempre son correctas (cambia esto por tu lógica de autenticación real)
            return HttpResponse("<h1>Bienvenido</h1>")
        else:
            return HttpResponse("<h1>Error en la autenticación</h1>", status=401)

    # Si no es una petición POST, simplemente renderizamos el formulario
    return render(request, 'login.html')


def hello(request): 
    return HttpResponse("<h1>Hello World</h1>")

def about(request):
    return HttpResponse('About')