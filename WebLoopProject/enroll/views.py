from django.shortcuts import render
from .forms import Student_Enroll
from .models import User
from django.http import HttpResponseRedirect
# Create your views here.
def thanks(request):
     fd=Student_Enroll(request.POST)
     return render(request,'enroll/success.html')

def Student_view(request):
    if request.method=='POST':
        fd=Student_Enroll(request.POST)
        if fd.is_valid():
            fn=fd.cleaned_data['first_name']
            ln=fd.cleaned_data['last_name']
            em=fd.cleaned_data['email']
            cn=fd.cleaned_data['contact_number']
            add=fd.cleaned_data['address']
            inn=fd.cleaned_data['intrest']

            reg=User(name=fn+' '+ln,email=em,contact_number=cn,address=add,intrest=inn)
            reg.save()
            return HttpResponseRedirect('/enroll/success')
    else:
            fd=Student_Enroll()
    return render(request,'enroll/stdreg.html',{'form':fd})
