from django import forms

class StudentEnroll(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    email=forms.EmailField()
    comment=forms.SlugField()
    description=forms.CharField(widget=forms.Textarea())
    # image=forms.ImageField()

