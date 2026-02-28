from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact_number=models.IntegerField(max_length=15)
    address=models.CharField()
    intrest=models.CharField()
    