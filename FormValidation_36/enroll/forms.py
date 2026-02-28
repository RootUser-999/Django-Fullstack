from django import forms

class Student_Enroll(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    repassword=forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data=super().clean()
        valpwd=self.cleaned_data['password']
        valrepwd=self.cleaned_data['repassword']

        if valpwd != valrepwd:
            raise forms.ValidationError('Passwords Does Not Match')