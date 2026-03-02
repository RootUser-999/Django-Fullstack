from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
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

#login view
def user_login(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            fd=AuthenticationForm(request=request,data=request.POST)
            if fd.is_valid():
                uname=fd.cleaned_data['username']
                upassword=fd.cleaned_data['password']
                user=authenticate(username=uname,password=upassword)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged In Successfulyy')
                    return HttpResponseRedirect('/profile/')
        else:
            fd=AuthenticationForm()

        return render(request,'enroll/userlogin.html',{'form':fd})
    else:
        return HttpResponseRedirect('/profile/')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')