from django.db import models

# Create your models here.
class abstract(models.Model):
    name = models.CharField(max_length=100)
    age =models.IntegerField()
    date = models.DateField()

    class Meta:
        abstract = True

class student(abstract):
    roll_no = models.IntegerField()
    marks = models.IntegerField()
    date=None

class teacher(abstract):
    subject = models.CharField(max_length=100)

class contractor(abstract):
    payment = models.IntegerField()
