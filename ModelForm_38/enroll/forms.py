from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','password','email']
        labels={'name':'Enter Name','password':'Enter Password'}
        widgets={'password':forms.PasswordInput(),
                 'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Naam idr likh'})}
        error_message={'name':{'required':'Naam likho phely'},
                       'password':{'required':'Password Likho phely'}}
