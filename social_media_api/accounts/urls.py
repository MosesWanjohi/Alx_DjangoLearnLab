
from django.urls import path, include
from rest_framework import routers

from .views import RegisterUser, LoginUser 

urlpatterns = [
    path('/register', RegisterUser.as_view, name='register'),
    path('/login', LoginUser.as_view, name='login'),
    path('/profile', include('profiles.urls')),
]
