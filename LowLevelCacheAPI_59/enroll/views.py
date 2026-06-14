from django.shortcuts import render
from django.core.cache import cache
# Create your views here.
def course(request):
    data={'name':'jhon','roll':101}
    cache.set_many(data,30)
    fee=cache.get('name')
    return render(request, 'enroll/course.html', {'f':fee })
