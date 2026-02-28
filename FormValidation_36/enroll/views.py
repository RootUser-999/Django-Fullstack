from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Student_Enroll
# Create your views here.
def thanks(request):
    fd=Student_Enroll(request.POST)
    return render(request, 'enroll/success.html')

def student_view(request):
    if request.method=='POST':
        fd=Student_Enroll(request.POST)
        if fd.is_valid():
            print(f"name={fd.cleaned_data['name']}")
            print(f"password={fd.cleaned_data['password']}")
            print(f"rpassword={fd.cleaned_data['repassword']}")
            return HttpResponseRedirect('/enroll/success')
    else:
        fd=Student_Enroll()
    return render(request,'enroll/stdreg.html',{'form':fd})

