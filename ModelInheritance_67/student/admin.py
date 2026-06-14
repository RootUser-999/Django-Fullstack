from django.contrib import admin
from .models import student, teacher, contractor
# Register your models here.

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'date', 'roll_no', 'marks']
@admin.register(teacher)
class teacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'date', 'subject']

@admin.register(contractor)
class contractorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'date', 'payment']