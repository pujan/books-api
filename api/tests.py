import json

from book.models import Author, Book, Publisher
from rest_framework import status
from rest_framework.test import APITestCase


class APITests(APITestCase):
    def setUp(self):
        author = Author.objects.create(firstname='John', lastname='Smith',
                                       biography="John Smith's biography...")
        author.save()
        publisher = Publisher.objects.create(name='Books of World', url='https://www.bow.com',
                                             description='Description publisher "Books of World"')
        publisher.save()
        book = Book.objects.create(title='Programming in Python', isbn='5676549012', pages=123,
                                   rating=2.9, publisher=publisher)
        book.authors.add(author)
        book.save()
        book = Book.objects.create(title='Python for Experts', isbn='5672937283', pages=354,
                                   rating=4.7, publisher=publisher)
        book.authors.add(author)
        book.save()

    def fetch(self, endpoint):
        response = self.client.get(endpoint, format='json')
        return response.status_code, json.loads(response.content)

    def test_get_all_books(self):
        '''Ensure get all list of books.'''
        endpoint = '/books/'
        status_code, content = self.fetch(endpoint)
        self.assertEqual(status_code, status.HTTP_200_OK)
        self.assertNotEqual(content, [])
        self.assertEqual(len(content), 2)
        self.assertEqual(content, [
            {
                "id": 1,
                "title": "Programming in Python",
                "rating": 2.9,
                "isbn": "5676549012",
                "pages": 123,
                "publisher": {
                    "id": 1,
                    "name": "Books of World",
                    "url": "https://www.bow.com",
                    "description": 'Description publisher "Books of World"'},
                "authors": [
                    {"id": 1,
                     "firstname": "John",
                     "lastname": "Smith",
                     "photo": None,
                     "number_books": 2,
                     "biography": "John Smith's biography...",
                     "uri": "/authors/john-smith/"}],
                "uri": "/books/programming-in-python/"},
            {
                "id": 2,
                "title": "Python for Experts",
                "rating": 4.7,
                "isbn": "5672937283",
                "pages": 354,
                "publisher": {
                    "id": 1,
                    "name": "Books of World",
                    "url": "https://www.bow.com",
                    "description": 'Description publisher "Books of World"'},
                "authors": [
                    {
                        "id": 1,
                        "firstname": "John",
                        "lastname": "Smith",
                        "photo": None,
                        "number_books": 2,
                        "biography": "John Smith's biography...",
                        "uri": "/authors/john-smith/"
                        }
                    ],
                "uri": "/books/python-for-experts/"
                }])

    def test_get_one_book(self):
        endpoint = '/books/1/'
        status_code, content = self.fetch(endpoint)
        self.assertEqual(status_code, status.HTTP_200_OK)
        self.assertNotEqual(content, {})
        self.assertEqual(content,
                         {
                             'id': 1,
                             'title': 'Programming in Python',
                             'rating': 2.9,
                             'isbn': '5676549012',
                             'pages': 123,
                             'publisher': {
                                 'id': 1,
                                 'name': 'Books of World',
                                 'url': 'https://www.bow.com',
                                 'description': 'Description publisher "Books of World"'},
                             'authors': [
                                 {
                                     'id': 1,
                                     'firstname': 'John',
                                     'lastname': 'Smith',
                                     'number_books': 2,
                                     'photo': None,
                                     'biography': "John Smith's biography...",
                                     'uri': '/authors/john-smith/'}],
                             'uri': '/books/programming-in-python/'})

    def test_get_all_authors(self):
        endpoint = '/authors/'
        status_code, content = self.fetch(endpoint)
        self.assertEqual(status_code, status.HTTP_200_OK)
        self.assertNotEqual(content, [])
        self.assertEqual(content, [
            {'id': 1,
             'firstname': 'John',
             'lastname': 'Smith',
             'number_books': 2,
             'photo': None,
             'biography': "John Smith's biography...",
             'uri': '/authors/john-smith/'}])

    def test_get_one_author(self):
        endpoint = '/authors/1/'
        status_code, content = self.fetch(endpoint)
        self.assertEqual(status_code, status.HTTP_200_OK)
        self.assertNotEqual(content, {})
        self.assertEqual(content, {
            'id': 1,
            'firstname': 'John',
            'lastname': 'Smith',
            'number_books': 2,
            'photo': None,
            'biography': "John Smith's biography...",
            'uri': '/authors/john-smith/'})

    def test_get_all_publishers(self):
        endpoint = '/publishers/'
        status_code, content = self.fetch(endpoint)
        self.assertEqual(status_code, status.HTTP_200_OK)
        self.assertNotEqual(content, [])
        self.assertEqual(content, [
            {'id': 1,
             'name': 'Books of World',
             'url': 'https://www.bow.com',
             'description': 'Description publisher "Books of World"'}])

    def test_get_one_publisher(self):
        endpoint = '/publishers/1/'
        status_code, content = self.fetch(endpoint)
        self.assertEqual(status_code, status.HTTP_200_OK)
        self.assertNotEqual(content, {})
        self.assertEqual(content, {
            'id': 1,
            'name': 'Books of World',
            'url': 'https://www.bow.com',
            'description': 'Description publisher "Books of World"'})
