from django.shortcuts import render
from .forms import StudentRegistraion
# Create your views here.
def studentenroll(request):
    fd=StudentRegistraion(auto_id=True ,label_suffix=' ')
    return render(request, 'enroll/studentenroll.html',{'form':fd})