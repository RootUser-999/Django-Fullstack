from django.shortcuts import render
from .models import Student
from .forms import StudentForm
# Create your views here.

def home(request):
    students = Student.objects.all()
    # students = Student.objects.filter(name__exact='shah')
    
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
    else:
        form = StudentForm()
    return render(  request, 'school/home.html', {'students': students, 'form': form})

