from django.urls import path
from .views import std_view
urlpatterns = [
    path('',std_view),
]
