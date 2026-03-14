from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def setcookie(request):
    request.session['name']='Jhon'
    return render(request,'student/setcookie.html')

def check_cookie(request):
    if 'name' in request.session:
        name=request.session.get('name')
        request.session.modified=True
        return render(request,'student/checkcookie.html',{'name':name})
    else:
        return HttpResponse('Your Session Expired!!')

def dele_cookie(request):
    del request.session['name']
    request.session.flush()