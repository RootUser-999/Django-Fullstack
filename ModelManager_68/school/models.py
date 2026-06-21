from django.db import models
from .managers import CustomManager
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city =models.CharField(max_length=100)
    marks = models.IntegerField()
    pass_date = models.DateField()

    students = CustomManager()


