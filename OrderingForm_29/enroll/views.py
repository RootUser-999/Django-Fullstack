from django.shortcuts import render
from .forms import EnrollForm
# Create your views here.
def studentenroll(request):
    fd=EnrollForm()
    fd.order_fields(field_order=['first_name','last_name','email'])
    return render(request, 'enroll/stdregistration.html',{'form':fd})