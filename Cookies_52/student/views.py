from django.shortcuts import render

def set_session(request):
    request.session['name']='jhon'
    return render(request,'student/setsession.html')

def get_session(request):
    # name=request.session['name']
    name=request.session.get('name',default='Guest')
    return render(request,'student/getsession.html',{'name':name})

def del_session(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'student/delsession.html')      
