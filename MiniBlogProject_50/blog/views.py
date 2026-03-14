from django.shortcuts import render, get_object_or_404
from .forms import UserCreation,UserPost
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Post
# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'post':posts})

def user_signup(request):
    if request.method=='POST':
        form=UserCreation(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=UserCreation()
    return render(request,'blog/signup.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upassword=form.cleaned_data['password']
                user=authenticate(username=uname,password=upassword)
                if user is not None:
                    login(request, user) # <--- ADD THIS LINE HERE
                    return HttpResponseRedirect('/dashboard/')
        else:
            form=AuthenticationForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def user_post(request):
    posts=Post.objects.all()
    if request.method =='POST':
        form=UserPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request,'Blog Posted Successfully')
    else:
        form=UserPost()
    return render(request,'blog/dashboard.html',{'form':form,'post':posts})

@login_required
def update_post(request,id):
    post=get_object_or_404(Post, id=id, user=request.user)
    if request.method=='POST':
        form=UserPost(request.POST,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'Blog Updated Successfully')
            return HttpResponseRedirect('/dashboard/')
    else:
        form=UserPost(instance=post)
    return render(request,'blog/update.html',{'form':form})

@login_required
def delete_post(request,id):
    post=get_object_or_404(Post, id=id, user=request.user)
    post.delete()
    messages.success(request,'Blog Deleted Successfully')
    return HttpResponseRedirect('/dashboard/')