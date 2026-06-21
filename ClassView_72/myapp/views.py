from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import MyForm
# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

class MyView(View):
    name='shahzeb'
    def get(self, request):
        return render(request,'myapp/class.html', {'name': self.name})

# class MyView2(View):
#     name='shahzeb'
#     def get(self, request):
#         return render(request,'myapp/class2.html', {'name': self.name})

class ContactView(View):
    def get(self,request):
        form = MyForm()
        return render(request,'myapp/contact.html',{'form':form})

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name']
            return HttpResponse(f'Thank you, {name}!')
        return render(request,'myapp/contact.html',{'form':form})