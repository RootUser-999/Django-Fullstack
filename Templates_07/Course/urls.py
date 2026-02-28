from django.urls import path
from Course import views
urlpatterns = [
   path('cv/',views.course_view)
]
