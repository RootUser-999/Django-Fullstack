from django.shortcuts import render
from datetime import datetime,timedelta
# Create your views here.
def setsession(request):  
    response= render(request,'student/setsession.html')
    # response.set_cookie('name','ali',max_age=60)
    # response.set_cookie('name','ali',expires=datetime.utcnow()+timedelta(days=2))
    response.set_signed_cookie('name','don',salt='nm',expires=datetime.utcnow()+timedelta(days=2))
    return response

def getsession(request):
    # name=request.COOKIES['name']
    # name=request.COOKIES.get('name',"Guest")
    name=request.get_signed_cookie('name',default='Guest',salt='nm')
    # name=request.session['name']
    # name=request.session.get('name',default='Guest')

    return render(request, 'student/getsession.html',{'name':name})

def delsession(request):
    response =render(request,'student/delsession.html')
    response.delete_cookie('name')
    return response

    # if 'name' in request.session:
    #     del request.session['name']
    # return render(request, 'student/delsession.html')