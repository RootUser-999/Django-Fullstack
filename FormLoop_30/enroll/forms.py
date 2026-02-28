from django import forms

class StudentEnroll(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    key=forms.CharField(widget=forms.HiddenInput())