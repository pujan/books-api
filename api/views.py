from django.shortcuts import render
from rest_framework import viewsets, views, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import AuthorSerializer, PublisherSerializer, BookSerializer
from book.models import Author, Publisher, Book


# ViewSets define the view behavior.
class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PublisherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CountersView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        books = len(Book.objects.all())
        authors = len(Author.objects.all())
        publishers = len(Publisher.objects.all())

        return Response({'authors': authors, 'books': books, 'publishers': publishers})
