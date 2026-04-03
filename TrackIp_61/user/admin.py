from django.contrib import admin
from .models import Post
admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')
# Register your models here.
