
from rest_framework import mixins, generics
from .serializers import BookSerializer, AuthorSerializer
from .models import Book
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import serializers
class BookListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class =BookSerializer

#Creating a BookDetailView for retrieving a single book by ID
class BookDetailView(generics.DetailAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class =BookSerializer

#Creating a BookCreateView for adding a new book
class BookCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()   
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise serializers.ValidationError(f'Book with title "{title}" already exists')
        else:
            serializer.save()

#Creating a BookUpdateView for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()   
    serializer_class =BookSerializer

    def perform_update(self, data, serializer):
        if len (data['title']) == 0:
            raise serializers.ValidationError('Title cannot be empty')
        else:
            serializer.save()

    

#Creating a BookDeleteView for removing an existing book
class BookDeleteView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()   
    serializer_class =BookSerializer

    def perform_destroy(self, instance):
        instance.delete()
