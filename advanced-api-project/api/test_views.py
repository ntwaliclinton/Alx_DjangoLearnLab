from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client.login = APIClient()
        self.book_url = reverse('book-list')  # Replace 'book-list' with your URL name
        self.book_data = {
            'title': 'Test Book',
            'author': 'Author Name',
            'publication_year': 2021
        }

    def test_create_book(self):
        response = self.client.post(self.book_url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])

    def test_get_book(self):
        book = Book.objects.create(**self.book_data)
        response = self.client.get(reverse('book-detail', kwargs={'pk': book.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], book.title)

    def test_update_book(self):
        book = Book.objects.create(**self.book_data)
        updated_data = {
            'title': 'Updated Test Book',
            'author': 'New Author',
            'publication_year': 2022
        }
        response = self.client.put(reverse('book-detail', kwargs={'pk': book.id}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_data['title'])

    def test_delete_book(self):
        book = Book.objects.create(**self.book_data)
        response = self.client.delete(reverse('book-detail', kwargs={'pk': book.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books_by_title(self):
        Book.objects.create(title='Django Unchained', author='Quentin Tarantino', publication_year=2012)
        Book.objects.create(title='Python Crash Course', author='Eric Matthes', publication_year=2016)
        response = self.client.get(self.book_url + '?title=django')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Django Unchained')

    def test_search_books_by_author(self):
        Book.objects.create(title='Learning Python', author='Mark Lutz', publication_year=2013)
        Book.objects.create(title='Django for Beginners', author='William Vincent', publication_year=2018)
        response = self.client.get(self.book_url + '?search=Vincent')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'William Vincent')

    def test_order_books_by_publication_year(self):
        Book.objects.create(title='Django Unchained', author='Quentin Tarantino', publication_year=2012)
        Book.objects.create(title='Python Crash Course', author='Eric Matthes', publication_year=2016)
        response = self.client.get(self.book_url + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Django Unchained')
