from django.shortcuts import render

# Create your views here.
def course_view(request):
    return render(request,'course/course.html') 