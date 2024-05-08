from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import path
from django.contrib.auth import authenticate, login as auth_login

"""# es una vista
def login(request):
    return HttpResponse(request, 'login.html')

def hello(request): 
    return HttpResponse(request, 'login.html')

def about(request):
    return HttpResponse('About')"""

# es una vista
def login(request):
    return JsonResponse(request, 'login.html')

def hello(request):
    return HttpResponse("Bienvenidos a la clinica EL CURADOR")

def about(request):
    return HttpResponse('About')

def user_login(request):
    return render(request, 'myapp/login.html')