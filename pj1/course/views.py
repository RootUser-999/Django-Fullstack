from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def course_django(request):
    return HttpResponse("<h1>HELLO Django")

def course_python(request):
    return HttpResponse("<h1>Hello Python<h1>")