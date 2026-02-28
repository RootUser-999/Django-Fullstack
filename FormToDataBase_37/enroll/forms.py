from django import forms

class Student_Enroll(forms.Form):
    name=forms.CharField(error_messages={'required':'Please enter your name'})
    email=forms.EmailField(error_messages={'required':'Please enter your email'})
    password=forms.CharField(widget=forms.PasswordInput())


