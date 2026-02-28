from django.shortcuts import render
from .forms import StudentEnroll
from django.http import HttpResponseRedirect
# Create your views here.
def success(request):
    fd=StudentEnroll(request.POST)
    return render(request,'enroll/success.html')

def Student_view(request):
    if request.method=='POST':
        fd=StudentEnroll(request.POST)
        if fd.is_valid():
            name=fd.cleaned_data['name']
            password=fd.cleaned_data['password']
            email=fd.cleaned_data['email']
            comment=fd.cleaned_data['comment']
            description=fd.cleaned_data['description']

            print(f'Name: {name}')
            print(f'Password: {password}')
            print(f'email: {email}')
            print(f'Comments: {comment}')
            print(f'Description: {description}')
            return HttpResponseRedirect('/enroll/thanks')
    else:
        fd=StudentEnroll()
    return render(request, 'enroll/stdreg.html',{'form':fd})    