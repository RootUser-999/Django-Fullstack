from django.shortcuts import render

# Create your views here.
def set_session(request):
    request.session['name']='Jhon Wick'
    return render(request,'enroll/set.html')

def home(request):
    ct=request.session.get('count',0)
    newcount=ct+1
    request.session['count']=newcount
    name=request.session.get('name',default='Guest')
    return render(request,'enroll/home.html',{'c':newcount,'name':name})

def dele(request):
    if 'count' in request.session:
        del request.session['count']
        request.session.flush()
    return render(request,'enroll/del.html')
