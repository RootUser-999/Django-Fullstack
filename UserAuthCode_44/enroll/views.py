from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def sign_up(request):
    if request.method=='POST':
        fd=UserCreationForm()
        if fd.is_valid():
            fd.save()
    else:
        fd=UserCreationForm()
    return render(request,'enroll/signup.html',{'form':fd})