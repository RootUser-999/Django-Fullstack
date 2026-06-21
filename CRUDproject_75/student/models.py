from django.db import models

# Create your models here.

class Student(models.Model):
    roll_number = models.IntegerField( unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name