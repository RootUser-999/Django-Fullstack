from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Post
from .forms import CustomUserCreationForm, Post_form
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'user/home.html',{'posts': posts})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return HttpResponseRedirect('/post/post/')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('/login/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return HttpResponseRedirect('/')


def user_post(request):
    if request.method == 'POST':
        form = Post_form(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, 'Post created successfully.')
            return HttpResponseRedirect('/post/post/')
    else:
        ip=request.session.get('ip',0)
        form = Post_form()
    return render(request, 'user/post.html', {'form': form,'ip':ip})

