from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book,Author
class BookApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(user=self.user)
        
        self.author=Author.objects.create(
            name='new author'

        )
        self.book = Book.objects.create(
            title='Test Book',
            author=self.author,
            publication_year=2022
        )
        
        self.book_data = {
            'title': 'New Book',
            'author': 1,
            'publication_year': 2023
        }
        
        self.url = reverse('book-list')

    def test_create_book(self):
        response = self.client.post('/books/create',self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(title='New Book').author, 'New Author')
    def test_get_book_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)