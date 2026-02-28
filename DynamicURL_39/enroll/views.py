from django.shortcuts import render

# Create your views here.
def show_subdetails(request,my_id,my_subid):
    if my_id == '1' and my_subid == '1':
        my_id = {'id':my_id, 'name':'Shahzaib', 'course':'Python', 'info':'This is sub details of student 1'}
    elif my_id == '2':
        my_id = {'id':my_id, 'name':'Ali', 'course':'Django'} 
           
    return render(request, 'enroll/show.html',{'id':my_id})

def show_details(request,my_id):
    if my_id == '1':
        my_id = {'id':my_id, 'name':'Shahzaib', 'course':'Python'}
    elif my_id == '2':
        my_id = {'id':my_id, 'name':'Ali', 'course':'Django'} 

    return render(request, 'enroll/show.html',{'id':my_id})

def home(request):
    return render(request,'enroll/home.html')