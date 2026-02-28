from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField()
    password=models.CharField()
    email=models.EmailField()