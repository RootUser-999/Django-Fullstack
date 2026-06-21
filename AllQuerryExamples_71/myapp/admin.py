from django.contrib import admin
from .models import Page, Post, Song
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('page_title','page_content','page_date_posted','page_author')
   

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title','post_content','post_date_posted','post_author')
    

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('song_title','song_content','song_date_posted','song_author')
    