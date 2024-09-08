from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Book

#Testing CRUD operations for Book model endpoints

class BookListViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('book-list')
    def test_book_list_view(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

