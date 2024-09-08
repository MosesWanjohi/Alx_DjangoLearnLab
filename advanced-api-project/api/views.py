
from rest_framework import mixins, generics
from .serializers import BookSerializer, AuthorSerializer
from .models import Book
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import serializers
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


#Creating a BookDetailView for retrieving a single book by ID
class BookDetailView(generics.DetailAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


#Creating a BookCreateView for adding a new book
class BookCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser]
    queryset = Book.objects.all()   
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        title = serializer.validate_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise serializers.ValidationError('Book with {self.title} already exists')
        else:
            serializers.save()

#Creating a BookUpdateView for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser]
    queryset = Book.objects.all()   
    serializer_class =BookSerializer

    def perform_update(self, data, serializer):
        if len (data['title']) > 50:
            raise serializers.ValidationError('Title is too long')
        else:
            serializer.save()

    

#Creating a BookDeleteView for removing an existing book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()   
    serializer_class =BookSerializer

    def perform_destroy(self, instance):
        instance.delete()
