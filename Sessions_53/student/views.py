from django.shortcuts import render

# Create your views here.
def set_session(request):
    request.session['name']='Jhon'
    request.session['lname']='Wick'
    return render(request,'student/setsession.html')

def get_session(request):
    name=request.session.get('name',default='Guest')
    lname=request.session.get('lname',default='User')
    # age=request.session.setdefault('age','26')
    keys=request.session.keys()
    items=request.session.items()
    return render(request,'student/getsession.html',{'name':name,'lname':lname,'key':keys,'items':items})

def del_session(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    return render(request,'student/delsession.html')
