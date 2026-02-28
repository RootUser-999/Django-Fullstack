from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def teach(request):
    return HttpResponse('<h1>ANONYMOUS<h1>')
