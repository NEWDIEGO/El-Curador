from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import path
from django.shortcuts import render

# es una vista

def login(request):
    # Tu lógica de login aquí
    return render(request, 'login.html')

def hello(request): 
    return HttpResponse("<h1>Hello World</h1>")

def about(request):
    return HttpResponse('About')