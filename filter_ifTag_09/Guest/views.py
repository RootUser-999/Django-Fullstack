from django.shortcuts import render

# Create your views here.
userType="guest"
userName="shahzeb"
dect={'ut':userType,'un':userName}

def guest_view(request):
    return render(request,'guest/guestone.html',dect)

def guest_two(request):
    return render(request,'guest/guesttwo.html',dect)