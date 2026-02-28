from django.urls import path
from . import views
urlpatterns = [
    path('adminek/',views.admin_view),
    path('admindo/',views.admin_two)
]