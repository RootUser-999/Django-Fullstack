from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from .forms import SignUpForm
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'enroll/signup.html', {'form': form})
def home(request):
    return render(request, 'enroll/home.html')

def user_login(request):
    fd=AuthenticationForm()
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
        return render(request,'enroll/login.html',{'form':fd})
    else:
        return HttpResponseRedirect('/profile/')
def profile(request):
    return render(request,'enroll/profile.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')