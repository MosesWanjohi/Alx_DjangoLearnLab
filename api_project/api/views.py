
#Using a simple view

from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import ObtainAuthToken
# Create your views here.
#Setting up a view that uses the serializer to retrieve and return book data.
class BookListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    def obtain_auth_token(self, request, username, password):
        username = request.data['username']
        password = request.data['password']
        user = TokenAuthentication(request, username=username, password=password)
        return user
    
    permission_classes = [IsAuthenticated]   
    queryset = Book.objects.all()
    serializer_class = BookSerializer

 

# Implementing CRUD Operations with ViewSets and Routers 
# in Django REST Framework using ViewSets

#from rest_framework import viewsets

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    def obtain_auth_token(self, request, username, password):
        username = request.data['username']
        password = request.data['password']
        user = TokenAuthentication(request, username=username, password=password)
        return user
    
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
 

