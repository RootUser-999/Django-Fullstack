from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('stuid','stuname')

# admin.site.register(models.Student,StudentAdmin) 

