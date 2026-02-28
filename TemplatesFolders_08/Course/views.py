from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cvone(request):
    return render(request, 'course/courseone.html')

def cvtwo(request):
    return render(request, 'course/coursetwo.html')