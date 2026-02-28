from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>WellCome Home<h1>")

def Course_view(request):
    return HttpResponse("<ul><li>ICT<li> ICT<li> DSA <li> PF<li><ul>")