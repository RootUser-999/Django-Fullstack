from django.urls import path
from . import views

urlpatterns = [
    path('services/',views.contact_view,name='contact'),
    path('success/',views.thanks_view),
]

