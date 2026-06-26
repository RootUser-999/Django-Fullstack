from django.db import models


class Student(models.Model):
    """Student model for generic class examples."""

    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.age})"

