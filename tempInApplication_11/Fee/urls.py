from django.urls import path
from . import views
urlpatterns = [
    path('fv/',views.fee_view)
]
