
from django.urls import path
from Course import views
urlpatterns = [
    path('cvone/',views.cvone),
    path('cvtwo/',views.cvtwo)
]