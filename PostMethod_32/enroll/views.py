from django.shortcuts import render
from . import forms
# Create your views here.
def std_view(request):
    fd=forms.StudentEnroll()
    return render(request,'enroll/stdreg.html',{'form':fd})