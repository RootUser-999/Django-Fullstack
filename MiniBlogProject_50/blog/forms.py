from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post

class UserCreation(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

class UserPost(forms.ModelForm):
    description=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=Post
        fields=['title','description']
    