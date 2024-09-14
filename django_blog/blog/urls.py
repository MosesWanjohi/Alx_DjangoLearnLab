
from django.urls import path
from .import views


urlpatterns = [
    path('register/', views.register, name='register'),  # Registration URL
    path('login/', views.user_login, name='login'),      # Login URL
    path('logout/', views.user_logout, name='logout'),   # Logout URL
    path('profile/', views.profile, name='profile'),     # Profile URL
]



