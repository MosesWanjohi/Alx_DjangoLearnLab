from rest_framework import mixins, generics
from .serializers import BookSerializer, AuthorSerializer
from django.contrib.auth.models import Book, Author

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


#Creating a BookDetailView for retrieving a single book by ID
class BookDetailView(generics.DetailAPIView):
    queryset = Book.objects.filter('{<pk>}: {<pk>}')   
    serializer_class =BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


#Creating a BookCreateView for adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()   
    serializer_class =BookSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#Creating a BookUpdateView for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()   
    serializer_class =BookSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

#Creating a BookDeleteView for removing an existing book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()   
    serializer_class =BookSerializer

    def post(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)