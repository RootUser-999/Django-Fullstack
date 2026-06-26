from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    age = forms.IntegerField(required=False)
    # enrollment_date = forms.DateField(required=True)
    course = forms.CharField(max_length=100, required=True)

