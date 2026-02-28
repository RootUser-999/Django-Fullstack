from django.shortcuts import render
from . import forms
# Create your views here.
def student_enroll(request):
    fd=forms.StudentEnroll()
    return render(request,'enroll/stdreg.html',{'form':fd})
