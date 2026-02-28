from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def services(request):
    return render(request, 'services/services.html')

def about(request):
    return render(request, 'about/about.html')