from django.shortcuts import render
from django.http import HttpResponseRedirect 
from . import forms
# Create your views here.
def thank(request):
    fd=forms.StdEnroll(request.POST)
    # name=fd.data['name']
    return render(request,'enroll/success.html')

def std_view(request):
    if request.method == 'POST':
        fd=forms.StdEnroll(request.POST)
        if fd.is_valid():
            name=fd.cleaned_data['name']
            password=fd.cleaned_data['password']
            email=fd.cleaned_data['email']

            print(f'Name={name}')
            print(f'Password={password}')
            print(f'Email={email}')
            return HttpResponseRedirect('/enroll/success')
            # return render(request,'enroll/success.html',{'nm':name})            

    else:
        fd=forms.StdEnroll()

    return render(request,'enroll/stdreg.html',{'form':fd})            
