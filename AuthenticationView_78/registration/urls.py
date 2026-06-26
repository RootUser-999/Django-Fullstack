from .views import profile
from django.urls import path

urlpatterns = [
    path('profile/',profile,name='profile'),
    
]

