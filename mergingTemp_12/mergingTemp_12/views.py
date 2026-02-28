from django.shortcuts import render

dict={'nm':'shahzab' , 'ut': 'Admin'}

def home(request):
    return render(request,'home/home.html',dict)