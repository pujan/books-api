from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#from django.contrib.auth.mixins import LoginRequiredMixin

from book.models import Author, Book, Publisher

class AuthorListView(ListView):
    model = Author
    template_name = 'book/authors.html'
    prepopulated_fields = {'slug': ('firstname', 'lastname')}


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'book/author_detail.html'


class BookListView(ListView):
    model = Book
    template_name = 'book/books.html'
    prepopulated_fields = {'slug': ('title',)}


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'


class PublisherListView(ListView):
    model = Publisher
    template_name = 'book/publishers.html'
    prepopulated_fields = {'slug': ('name',)}


class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'book/publisher_detail.html'


