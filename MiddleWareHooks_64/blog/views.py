from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Home")

def process(request):
    return HttpResponse("Process view")

def exc(request):
    a=10/0
    return HttpResponse("Exception view")
