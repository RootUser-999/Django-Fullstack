from django.urls import path
from . import views
urlpatterns = [
    path('guestone/',views.guest_view),
    path('guesttwo/',views.guest_two)
    ]