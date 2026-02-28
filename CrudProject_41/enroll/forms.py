from django import forms
from .models import Student
class StudentRegistration(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        # fields=['name','password','email']
        widgets={'password':forms.PasswordInput(render_value=True)}