from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from accounts.models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.validators import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
# Create your views here.

#User registration ApiView

class RegisterUserView(APIView):
#Getting data from user registration request
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

    #Data validation
        if not username or not password or not email:
            raise ValidationError('Please provide username, password and email')
    
    #New user registration
        user = CustomUser.objects.create_user(username=username, password=password, email=email)

        return Response({'message':'User registered successfully'})
    
    #User login ApiView
class LoginUserView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        user = CustomUser.objects.filter(username=username, password=password)

        if user:
            return Response({'message':'User logged in successfully'})

        else:
            return Response({'message':'Invalid credentials'})

class UserProfileView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        data = {
            'username': user.username,
            'email': user.email,
            'bio': user.bio,
            'profile_picture': user.profile_picture,
            'followers': user.followers.count(),
        }
       
        return Response(request.data)

    def put(self, request, format=None):
        user = request.user
        user.profile_picture = request.data.get('profile_picture')
        user.bio = request.data.get('bio')
        user.save()
        return Response({'message': 'Profile updated successfully'})
    
#Creating endpoints for Managing Followers
#Follow Management Views:

User = get_user_model()

#Function based view for following user
@login_required
def follow_user(request, user_id):
    user_to_follow = User.objects.all().filter(User, id=user_id)
    request.user.following.add(user_to_follow)
    return redirect('profile', user_id=user_id)

#Function based view for unfollowing user
@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = User.objects.all().filter(User, id=user_id)
    request.user.following.remove(user_to_unfollow)
    return redirect('profile', user_id=user_id)

