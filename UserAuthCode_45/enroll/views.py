from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
# Create your views here.

def sign_up(request):
    if request.method=='POST':
        fd=SignUpForm(request.POST)
        if fd.is_valid():
            fd.save()
            messages.success(request,'Account Created Successfully !!')
    else:
        fd=SignUpForm()
    return render(request,'enroll/signup.html',{'form':fd})