from django.shortcuts import render

# Create your views here.
def ser_view(request):
    return render (request, 'ser/service.html')