from django.shortcuts import render
from .forms import UserCreation
# Create your views here.
def user_signup(request):
    if request.method=='POST':
        fd=UserCreation(request.POST)
        if fd.is_valid():
            fd.save()
    else:
        fd=UserCreation()
    return render(request,'enroll/signup.html',{'form':fd})