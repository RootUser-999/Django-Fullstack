from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=20)
    stuemail=models.EmailField(max_length=30)
    stupass=models.CharField(max_length=30)