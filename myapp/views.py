from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.

def hello(request): 
    return HttpResponse("<h1>Hello World</h1>")

def about(request):
    return HttpResponse('About')