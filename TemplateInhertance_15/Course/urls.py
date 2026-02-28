from django.urls import path
from . import views
urlpatterns = [
    path('cview/',views.course_view)
]