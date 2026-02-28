from django.shortcuts import render

# Create your views here.
def edu_veiw(request):
    return render(request, 'edu/education.html')