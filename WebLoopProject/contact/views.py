from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from django.http import HttpResponseRedirect
# Create your views here.
def thanks_view(request):
    return render(request,'contact/success.html')
def contact_view(request):
    if request.method =='POST':
        data=ContactForm(request.POST)
        if data.is_valid():
            nm=data.cleaned_data['name']
            em=data.cleaned_data['email']
            msg=data.cleaned_data['message']
            reg=Contact(name=nm,email=em,message=msg)
            reg.save()
            return HttpResponseRedirect('/contact/success')
    else:
        data=ContactForm()
    return render(request,'contact/contact.html',{'form':data})