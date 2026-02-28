from django.urls import path
from Fee import views
urlpatterns = [
   path('fee/',views.fee_view)
]
