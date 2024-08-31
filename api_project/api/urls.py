from django.urls import path
from .views import BookListListAPIView

urlpatterns = [
    path('books/', BookListListAPIView.as_view(), name = 'book-list')
]