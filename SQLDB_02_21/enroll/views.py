from django.shortcuts import render
from enroll.models import Student
# Create your views here.
def student_view(request):
    std=Student.objects.all()
    return render(request, 'enroll/enroll.html',{'stu':std})