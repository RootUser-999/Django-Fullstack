from django.shortcuts import render
from .forms import Student,Teacher
# Create your views here.
def student_show(request):
    if request.method=='POST':
        fd=Student(request.POST)
        if fd.is_valid():
            fd.save()
    else:
        fd=Student()
    return render(request,'enroll/std.html',{'form':fd})

def teacher_registration(request):
    if request.method=='POST':
        fd=Teacher(request.POST)
        if fd.is_valid():
            fd.save()
    else:
        fd=Teacher()
    return render(request,'enroll/teacher.html',{'form':fd})

