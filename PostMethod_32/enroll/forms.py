from django import forms

class StudentEnroll(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    email=forms.EmailField()
