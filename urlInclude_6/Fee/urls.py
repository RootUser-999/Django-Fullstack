from django.urls import path
from Fee import views
urlpatterns=[
    path('fv/',views.fee_view),
    path('voucher/',views.fee_voucher)

]