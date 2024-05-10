from django.shortcuts import render
from django.http import HttpResponse

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