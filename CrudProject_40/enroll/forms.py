from django import forms
from .models import Student
class StudentRegistration(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','email','password']
    # name=forms.CharField()
    # email=forms.EmailField()
    # password=forms.CharField(widget=forms.PasswordInput())
        widgets={'password':forms.PasswordInput(render_value=True)}