from django.shortcuts import render
from .forms import Student_Enroll
from .models import User
# Create your views here.

def Student_view(request):
    if request.method =='POST':
        fd=Student_Enroll(request.POST)
        if fd.is_valid():
           nm=fd.cleaned_data['name']
           em=fd.cleaned_data['email']  
           ps=fd.cleaned_data['password']
           print(nm,em,ps)
           reg=User(name=nm,email=em,password=ps)
           reg.save() 
    else: 
        fd=Student_Enroll()
    return render(request,'enroll/stdreg.html',{'form':fd})        