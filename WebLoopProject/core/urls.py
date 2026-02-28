from django.urls import path
from . import views
urlpatterns = [
    path('services/',views.services,name='services'),
    path('thanks/',views.about,name='about'),
]
