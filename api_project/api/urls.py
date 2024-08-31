from django.urls import path, include
from .views import BookListAPIView, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet)
urlpatterns = [
    path('books/', BookListAPIView.as_view(), name = 'book-list'),
    path('', include(router.urls)),
]