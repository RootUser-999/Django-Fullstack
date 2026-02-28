from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Home Page<h1>")

def std_list(request):
    return HttpResponse("<h1>Shahzeb<h1>")

