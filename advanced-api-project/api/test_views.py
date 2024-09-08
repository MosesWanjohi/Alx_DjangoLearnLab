from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Book, Author

#Testing CRUD operations for Book model endpoints

class BookListViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('book-list')
        #Creating a book 
        self.author = Author.objects.create(name='MC Kogi')
        self.book = Book.objects.create(
            title='Take That Shot',
            publication_year=2023,
            author= self.author
        )
    def test_book_list_view(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
    
class BookCreateViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('book-list')
        self.author = Author.objects.create(name='MC Kogi')
        self.book_data = {
            'title': 'Take That Shot',
            'publication_year': 2023,
            'author': self.author.id # 1
        }

    def test_book_create_view(self):
        response = self.client.post(self.url, self.book_data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), '1') # 1 (MC Kogi)
        self.assertEqual(Book.objects.get().title, 'Take That Shot')

class BookRetrieveViewTestCase(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title='Take That Shot',
            publication_year=2023,
            author=self.author
        )
        self.url = reverse('book-detail', args=[self.book.id])

    def test_book_retrieve_view(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Take That Shot')
        self.assertEqual(response.data['publication_year'], 2023)

#Running tests with python manage.py test

