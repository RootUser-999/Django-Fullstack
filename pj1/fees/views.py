from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fee_django(request):
    return HttpResponse("<h1>Hello FEE django<h1>")
def fee_python(request):
    return HttpResponse("<h1>HEllo fee python<h1>")