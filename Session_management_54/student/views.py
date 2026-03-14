from django.shortcuts import render

# Create your views here.
def set_session(request):
    request.session['name']='Jhon'
    return render(request,'student/setsession.html')

def get_session(request):
    name=request.session.get('name',default='guest')
    return render(request,'student/getsession.html',{'name':name})

def del_session(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    return render(request,'student/delsession.html')
