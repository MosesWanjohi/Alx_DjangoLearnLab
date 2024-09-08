from django.shortcuts import render
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


# Create your views here.
class BookView(ApiView):
    