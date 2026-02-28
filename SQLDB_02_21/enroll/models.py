from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.CharField(max_length=20, primary_key=True)
    stuname=models.CharField(max_length=20)
    stusex=models.CharField(max_length=10)
    stubirth=models.DateField()
    