from django.shortcuts import render
from .models import student, teacher, contractor
# Create your views here.

def home(request):
    s = student.objects.all()
    t = teacher.objects.all()
    c = contractor.objects.all()
    return render(request, 'student/home.html', {'s': s, 't': t, 'c': c})