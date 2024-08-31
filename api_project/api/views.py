from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

# Create your views here.
#Setting up a view that uses the serializer to retrieve and return book data.
class BookListListAPIView(generics.ListAPIView):
    querryset = Book.objects.all()
    serializer_class = BookSerializer
    
