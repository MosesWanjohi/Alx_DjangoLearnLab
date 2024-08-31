
#Using a simple view

from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

# Create your views here.
#Setting up a view that uses the serializer to retrieve and return book data.
class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Implementing CRUD Operations with ViewSets and Routers 
# in Django REST Framework using ViewSets

from rest_framework import viewsets

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

