from Course import views
from django.urls import path

urlpatterns=[
    path('',views.home),
    path('cv/',views.course_view)
]