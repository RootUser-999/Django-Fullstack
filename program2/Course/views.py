from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1 style{color:"blue"}>Home Page<h1>')
def learn_web(request):
    return HttpResponse('<h1>Web Development With Django<h1>')
# Create your views here.
