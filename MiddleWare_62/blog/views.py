from django.shortcuts import render
from django.http import HttpResponse
from .middlewares import my_middleware

# Create your views here.
def home(request):
    return HttpResponse('home page')