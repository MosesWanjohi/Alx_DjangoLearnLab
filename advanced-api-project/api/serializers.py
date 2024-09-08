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
        for publication_year in fields:
            if publication_year > 'publication_year':
                raise serializers.ValidationError('Publication year cannot be in the future')
            





#Creating AuthorSerializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'BookSerializer(serializers.ModelSerializer)']
