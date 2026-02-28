from django import forms

class Student_Enroll(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email=forms.EmailField(max_length=100)
    contact_number=forms.IntegerField()
    address=forms.CharField(widget=forms.Textarea())
    intrest=forms.CharField(widget=forms.Textarea)
    