from django import forms

class StdEnroll(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    email=forms.EmailField()