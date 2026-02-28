from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fd=StudentRegistration(request.POST)
        if fd.is_valid():
            # std=Student(name=fd.cleaned_data['name'], email=fd.cleaned_data['email'], password=fd.cleaned_data['password'])
            fd.save()
            fd=StudentRegistration()        

    else:
        fd=StudentRegistration()
    stud=Student.objects.all()        
    return render(request, 'enroll/addShow.html',{'form':fd,'stu':stud})

# delete function
def delete_data(request,id):
    if request.method == 'POST':
        id=Student.objects.get(pk=id)
        id.delete()
        return HttpResponseRedirect('/')
# update
def update_data(request,id):
    if request.method == 'POST':
        pi=Student.objects.get(pk=id)
        fd =StudentRegistration(request.POST,instance=pi)
        if fd.is_valid():
            fd.save()
    else:
        pi=Student.objects.get(pk=id)
        fd =StudentRegistration(instance=pi)
    return render(request, 'enroll/update.html',{'form':fd,'id':id})
