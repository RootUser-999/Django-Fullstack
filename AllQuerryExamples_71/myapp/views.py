from django.shortcuts import render
from .models import Page, Post, Song

def home(request):

    pages = Page.objects.all()
    posts = Post.objects.all()
    songs = Song.objects.all()

    return render(
        request,
        'myapp/home.html',
        {
            'pages': pages,
            'posts': posts,
            'songs': songs
        }
    )