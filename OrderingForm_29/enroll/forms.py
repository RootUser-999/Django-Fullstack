from django import forms

class EnrollForm(forms.Form):
    last_name=forms.CharField()
    email=forms.EmailField()
    first_name=forms.CharField()
    