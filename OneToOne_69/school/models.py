from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    # user=models.OneToOneField(User, on_delete=models.CASCADE)
    # user=models.OneToOneField(User, on_delete=models.PROTECT)
    user=models.OneToOneField(User, on_delete=models.CASCADE,limit_choices_to={'is_staff':True})
    roll=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

