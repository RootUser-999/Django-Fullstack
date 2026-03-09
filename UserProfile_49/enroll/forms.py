from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserCreation(UserCreationForm):
    class Meta:
        model=User
        fields=['Username','First_name','Last_name']


