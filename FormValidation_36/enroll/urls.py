from django.urls import path
from . import views
urlpatterns=[
    path('',views.student_view),
    path('success/',views.thanks)
]