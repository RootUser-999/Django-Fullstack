from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def Student_view(request):
    if request.method=='POST':
        data=StudentRegistration(request.POST)
        if data.is_valid():
            nm=data.cleaned_data['name']
            pwd=data.cleaned_data['password']
            email=data.cleaned_data['email']
            print(f'name: {nm} \n password:{pwd} \n email: {email}')

    else:
        data=StudentRegistration()
    return render(request,'enroll/stdreg.html',{'form':data})    
