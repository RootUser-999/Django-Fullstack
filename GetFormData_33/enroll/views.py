from django.shortcuts import render
from . import forms
# Create your views here.
def Std_view(request):
    if request.method =='POST':
        fd=forms.StdEnroll(request.POST)
        if fd.is_valid():
            # bad approch
            # name=request.POST['name']

            name=fd.cleaned_data['name']
            password=fd.cleaned_data['password']
            email=fd.cleaned_data['email']

            print(f'name={name}')
            print(f'password={password}')
            print(f'email={email}')
            

        

    else:
        fd=forms.StdEnroll()
        print('yee get req sy aya hai')    
    return render(request,'enroll/stdreg.html',{'form':fd})