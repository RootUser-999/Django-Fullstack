from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def user_signup(request):
    if request.method=='POST':
        fd=UserCreationForm(request.POST)
        if fd.is_valid():
            fd.save()
            messages.success(request,'Account Created Successfulyy')
    else:
        fd=UserCreationForm()
    return render(request,'enroll/signup.html',{'form':fd})

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
                    messages.success(request,'Logged In Succcessfully')
                    # us=request.fd.objects.all()
                    return HttpResponseRedirect('/profile/')
        else:
            fd=AuthenticationForm()

        return render(request,'enroll/login.html',{'form':fd})
    else:
        # us.request.user.objects
        return HttpResponseRedirect('/profile/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
def profile(request):
    return render(request,'enroll/profile.html')