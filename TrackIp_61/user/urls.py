from django.urls import path
from . import views
urlpatterns = [
    # path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('post/', views.user_post, name='post'),
]