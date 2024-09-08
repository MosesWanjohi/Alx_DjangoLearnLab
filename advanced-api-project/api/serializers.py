#Creating Custom Serializers

from rest_framework import serializers
from .models import Book, Author
from datetime import datetime
#Creating a BookSerializer
class BookSerializer(serializers.ModelSerializer):
    publication_year = datetime.now()
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author'] # or fields = '__all__'
        
        #Adding custom validation to the BookSerializer to ensure the publication_year is not in the future.
        for publication_year in fields:
            if publication_year > 'publication_year':
                raise serializers.ValidationError('Publication year cannot be in the future')


#Creating AuthorSerializer
class AuthorSerializer(serializers.ModelSerializer):
    
    #A nested BookSerializer to serialize the related books dynamically.
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']