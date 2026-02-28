from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fee_view(request):
    return render(request,'fee_view.html')