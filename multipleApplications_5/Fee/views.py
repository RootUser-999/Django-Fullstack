from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fee_view(request):
    return HttpResponse("<h1>Fee Paid<h1>")