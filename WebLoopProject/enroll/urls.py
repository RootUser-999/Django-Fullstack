from django.urls import path
from . import views
urlpatterns = [
    path('',views.Student_view,name='enroll'),
    path('success/',views.thanks)
]
