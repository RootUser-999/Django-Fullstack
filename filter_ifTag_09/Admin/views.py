from django.shortcuts import render

# Create your views here.
user='guest'
name='shahzeb'
dict2={'u':user,'n':name}
def admin_view(request):
    return render(request,'admin/adminone.html',dict2)

def admin_two(request):
    return render(request,'admin/admintwo.html',dict2)