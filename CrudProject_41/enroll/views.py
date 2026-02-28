from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student
# Create your views here.
def home(request):
    if request.method=='POST':
        fd=StudentRegistration(request.POST)
        if fd.is_valid():
            fd.save()
            fd=StudentRegistration()
    else:
        fd=StudentRegistration()   
    stud=Student.objects.all()
    return render(request,'enroll/show.html',{'form':fd,'stud':stud})

# delete function 
def delete_data(request,id):
    if request.method == 'POST':
        id=Student.objects.get(pk=id)
        id.delete()
        return HttpResponseRedirect('/')
        
#update function
def update_function(request,id):
    if request.method=='POST':
        std=Student.objects.get(pk=id)
        fd=StudentRegistration(request.POST,instance=std)
        if fd.is_valid():
            fd.save()
    else:
        std=Student.objects.get(pk=id)
        fd=StudentRegistration(instance=std)
    return render(request,'enroll/update.html',{'form':fd,'std':id})
