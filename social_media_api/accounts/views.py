from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from accounts.models import CustomUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.validators import ValidationError
# Create your views here.

#User registration ApiView

class RegisterUser(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [AllowAny]

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
    class LoginUser(APIView):
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [IsAuthenticated]

        def post(self, request, format=None):
            username = request.data.get('username')
            password = request.data.get('password')

            user = CustomUser.objects.filter(username=username, password=password)

            return Response({'message':'User logged in successfully'})

