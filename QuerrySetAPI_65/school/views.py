from django.shortcuts import render
from .models import Student, Teacher
# Create your views here.


def home(request):
    data = Student.objects.all()
    t_data = Teacher.objects.all()

    new_data= t_data.union(data)
    return render(request, 'school/home.html', {'data': data, 't_data': t_data})

