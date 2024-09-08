#Creating Custom Serializers

from rest_framework import serializers
from .models import Book, Author
from datetime import datetime
#Creating a BookSerializer
class BookSerializer(serializers.ModelSerializer):
    publication_year = datetime.now()
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author'] #fields = '__all__'






#Creating AuthorSerializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'BookSerializer(serializers.ModelSerializer)']
