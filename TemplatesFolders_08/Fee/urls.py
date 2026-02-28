from django.urls import path
from Fee import views
urlpatterns = [
    path('fvone/',views.fvone),
    path('fvtwo/',views.fvtwo)

    ]